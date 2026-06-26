import os
import re
import time
import groq
from groq import Groq
from dotenv import load_dotenv
from src.language import detect_language, get_language_instruction
from src.prompts import (
    SYSTEM_PROMPT, USER_TEMPLATE,
    is_greeting, get_greeting_response,
    is_meta_question, get_meta_answer,
    is_technical_question, get_technical_answer,
    format_retrieved_chunks,
    is_valid_source_name, clean_source_name,
)

# ── Fix: robust import for RateLimitError ──
try:
    from groq import RateLimitError
except ImportError:
    try:
        from groq.types import RateLimitError
    except ImportError:
        # Fallback: define a dummy class that never matches actual errors
        class RateLimitError(Exception):
            pass

load_dotenv()
_client = None
RELEVANCE_THRESHOLD = 0.35
MAX_HISTORY_TURNS = 4

# ── Model pool (in order of preference) ──
MODEL_POOL = [
    "qwen/qwen3-32b",
    "llama-3.3-70b-versatile",
    "gemma2-9b-it",
    "mixtral-8x7b-32768",
]

def get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file")
        _client = Groq(api_key=api_key)
    return _client


def strip_think_tags(text: str) -> str:
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def build_sources_line(used_chunks: list) -> str:
    sources = []
    seen = set()
    for chunk in used_chunks:
        src = chunk.source or ""
        if src and src not in seen and is_valid_source_name(src):
            seen.add(src)
            sources.append(clean_source_name(src))
    if not sources:
        return ""
    return "\n\n---\n📚 **Sources:** " + " · ".join(sorted(sources))


def ensure_citations(answer: str, used_chunks: list) -> str:
    if re.search(r'(Source|সূত্র|📚)', answer, re.IGNORECASE):
        return answer
    sources_line = build_sources_line(used_chunks)
    return answer + sources_line if sources_line else answer


def format_history_for_api(chat_history: list) -> list:
    filtered = [m for m in chat_history if m["role"] in ("user", "assistant")]
    max_messages = MAX_HISTORY_TURNS * 2
    recent = filtered[-max_messages:] if len(filtered) > max_messages else filtered
    api_messages = []
    for msg in recent:
        api_messages.append({"role": msg["role"], "content": msg["content"]})
    return api_messages


def get_last_topic(chat_history: list) -> str:
    for msg in reversed(chat_history):
        if msg["role"] == "user":
            q = msg["content"].strip()
            if len(q) > 10 and not is_greeting(q):
                return q
    return ""


def rewrite_query(query: str, chat_history: list, lang_code: str) -> str:
    if not chat_history or len(query.split()) > 8:
        return query

    reference_words = [
        'এর', 'ওর', 'এটা', 'ওটা', 'এই', 'ওই', 'সেটা', 'এটি',
        'আরো', 'আরও', 'বিস্তারিত', 'বলো', 'বলুন', 'কি', 'কী',
        'er', 'eta', 'ota', 'aro', 'bolo', 'bolun',
        'it', 'its', 'this', 'that', 'more', 'details', 'further'
    ]
    query_lower = query.lower()
    if not any(ref in query_lower for ref in reference_words):
        return query

    last_messages = chat_history[-4:] if len(chat_history) >= 4 else chat_history
    context = "\n".join([
        f"{m['role'].upper()}: {m['content'][:200]}"
        for m in last_messages
    ])

    client = get_client()
    try:
        response = client.chat.completions.create(
            model=MODEL_POOL[0],
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a query expansion assistant. Given a conversation history "
                        "and a follow-up question, rewrite the follow-up question to be "
                        "self-contained and specific. Keep it short. "
                        "Output ONLY the rewritten query, nothing else."
                    )
                },
                {
                    "role": "user",
                    "content": f"Conversation:\n{context}\n\nFollow-up question: {query}\n\nRewritten query:"
                }
            ],
            max_tokens=100,
            temperature=0.0
        )
        rewritten = response.choices[0].message.content.strip()
        print(f"Query rewritten: '{query}' → '{rewritten}'")
        return rewritten if rewritten else query
    except Exception:
        return query


def generate(
    query: str,
    chunks: list,
    has_reliable: bool,
    lang_code: str,
    chat_history: list = None
) -> tuple:

    if chat_history is None:
        chat_history = []

    # ── 1. Greetings ──
    if is_greeting(query):
        return get_greeting_response(lang_code), []

    # ── 2. Technical questions ──
    if is_technical_question(query):
        return get_technical_answer(lang_code), []

    # ── 3. Identity / meta ──
    if is_meta_question(query):
        return get_meta_answer(lang_code), []

    # ── 4. Handle follow-up questions ──
    from src.prompts import is_followup_question
    actual_query = query
    if is_followup_question(query) and chat_history:
        last_topic = get_last_topic(chat_history)
        if last_topic:
            actual_query = f"{last_topic} — {query}"

    # ── 5. No reliable results ──
    if not has_reliable:
        if lang_code == 'bn':
            return (
                "দুঃখিত, এই বিষয়ে আমার ডকুমেন্টে পর্যাপ্ত তথ্য নেই। "
                "অনুগ্রহ করে স্থানীয় কৃষি সম্প্রসারণ কর্মকর্তার সাথে যোগাযোগ করুন।"
            ), []
        return (
            "I don't have reliable information on this in my knowledge base. "
            "Please consult your local agricultural extension office."
        ), []

    # ── 6. Build messages with history ──
    lang_instruction = get_language_instruction(lang_code)
    context = format_retrieved_chunks(chunks)
    system = SYSTEM_PROMPT.format(language_instruction=lang_instruction)

    script_note = 'Bengali Unicode script (বাংলা অক্ষরে লিখুন)' if lang_code == 'bn' else 'English'
    current_user_msg = (
        f"Context Documents (answer ONLY from these — ignore brief mentions like table cells):\n"
        f"{context}\n\n"
        f"Question: {actual_query}\n\n"
        f"⚠️ Reply in {script_note} only. "
        f"If context is insufficient, say so honestly."
    )

    history_messages = format_history_for_api(chat_history)
    messages = [{"role": "system", "content": system}]
    messages.extend(history_messages)
    messages.append({"role": "user", "content": current_user_msg})

    client = get_client()

    # ── 7. Model fallback loop ──
    last_exception = None
    for model in MODEL_POOL:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=1024,
                temperature=0.1
            )
            raw = response.choices[0].message.content
            answer = strip_think_tags(raw)

            used_chunks = [c for c in chunks if c.similarity_score >= 0.45]
            answer = ensure_citations(answer, used_chunks)
            return answer, used_chunks

        except RateLimitError as e:
            last_exception = e
            print(f"Rate limit hit for {model}: {e}. Trying next model...")
            time.sleep(1)
            continue

        except Exception as e:
            # Catch any other exception (e.g., network, API error) and try next model
            last_exception = e
            print(f"Unexpected error with {model}: {e}")
            # If it's a 429 (rate limit) but we didn't catch RateLimitError, also retry
            if hasattr(e, 'status_code') and e.status_code == 429:
                print("Detected 429 status – treating as rate limit.")
                time.sleep(1)
                continue
            continue

    # If all models fail, return a user‑friendly error message
    if lang_code == 'bn':
        err_msg = (
            "আমাদের সিস্টেম বর্তমানে উচ্চ চাহিদার সম্মুখীন। "
            "অনুগ্রহ করে কয়েক মিনিট পরে আবার চেষ্টা করুন। "
            "যদি সমস্যা থেকে যায়, সমর্থনের সাথে যোগাযোগ করুন।"
        )
    else:
        err_msg = (
            "Our system is currently experiencing high demand. "
            "Please try again in a few minutes. "
            "If the problem persists, contact support."
        )
    return err_msg, []