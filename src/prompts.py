import re

# ──────────────────────────────────────────────
# SYSTEM PROMPT — natural, expert tone
# ──────────────────────────────────────────────
SYSTEM_PROMPT = """You are AgroAdvisor BD, an expert agricultural advisor for Bangladesh.

━━━ LANGUAGE RULES ━━━
- Bengali script question → reply ONLY in Bengali Unicode script
- Romanized Bengali → reply ONLY in Bengali Unicode script
- English question → reply in English
- NEVER write Bengali words in Roman letters
- {language_instruction}

━━━ CRITICAL ANSWERING RULES ━━━
1. Use EXACT terms from the context — do NOT paraphrase chemical names,
   variety names, or quantities. If context says "Tricyclazole 0.75g/L",
   write exactly "Tricyclazole 0.75g/L", not a vague description.

2. Use EXACT numbers — if context says "220-250 kg/hectare", write that
   exact number, do not say "a moderate amount".

3. Use EXACT variety names — write "BRRI dhan29" not "high yield variety".

4. Structure your answer:
   - Start with a direct answer to the question
   - Use bullet points for lists
   - Bold key terms, dosages, and variety names
   - End with source citation

5. If context contains the answer, ALWAYS use it — do not say you lack
   information if the context clearly addresses the question.

6. Only say you lack information if context is truly irrelevant.

━━━ CITATION FORMAT ━━━
Always end with: (Source: filename, Page X) or Sources: file1, file2

━━━ IF NO INFORMATION ━━━
Bengali: "দুঃখিত, এই বিষয়ে আমার ডকুমেন্টে পর্যাপ্ত তথ্য নেই।"
English: "I don't have sufficient information on this topic."
"""

USER_TEMPLATE = """Context Documents (use EXACT terms, numbers, and names from these):
{context}

Question: {question}

Instructions:
- Answer in {'Bengali Unicode script' if question contains Bengali characters else 'English'}
- Use EXACT chemical names, variety names, and quantities from context
- Be specific and direct
- Do NOT paraphrase technical terms

Answer:"""

# ──────────────────────────────────────────────
# GREETING DETECTION
# ──────────────────────────────────────────────
GREETING_PATTERNS = [
    r'^(hi|hey|hello|good\s?(morning|afternoon|evening|night))[!,. ]*$',
    r'^(হ্যালো|হেই|আসসালামু|সালাম|নমস্কার|শুভ)[!,. ]*',
    r'^(tmi k\??|tumi k\??|apni k\??|ke tumi\??)',
    r'^(how are you|how r u|whats up|what\'s up)[!,. ?]*$',
    r'^(kemon acho|kemon achen|ki obostha)[!,. ?]*$',
]

GREETING_RESPONSES = {
    'en': (
        "Hello! 👋 I'm **AgroAdvisor BD** — your agricultural assistant for Bangladesh.\n\n"
        "I can help you with:\n"
        "- 🌾 **Crop diseases** — symptoms, causes, management\n"
        "- 🐛 **Pest control** — identification and treatment\n"
        "- 🌧️ **Climate impacts** — flood, drought, salinity effects\n"
        "- 🧪 **Fertilizer guidance** — dosage and timing\n"
        "- 🥦 **Vegetable & fruit farming** — production guides\n\n"
        "What crop issue can I help you with today?"
    ),
    'bn': (
        "হ্যালো! 👋 আমি **AgroAdvisor BD** — বাংলাদেশের কৃষি বিষয়ক সহকারী।\n\n"
        "আমি সাহায্য করতে পারি:\n"
        "- 🌾 **ফসলের রোগ** — লক্ষণ, কারণ ও প্রতিকার\n"
        "- 🐛 **পোকামাকড় দমন** — চিহ্নিতকরণ ও ব্যবস্থাপনা\n"
        "- 🌧️ **জলবায়ু প্রভাব** — বন্যা, খরা, লবণাক্ততা\n"
        "- 🧪 **সার ব্যবস্থাপনা** — মাত্রা ও প্রয়োগ সময়\n"
        "- 🥦 **সবজি ও ফল চাষ** — উৎপাদন গাইড\n\n"
        "আজকে কোন ফসল বা কৃষি বিষয়ে জানতে চান?"
    )
}

def is_greeting(query: str) -> bool:
    q = query.strip().lower()
    return any(re.search(p, q, re.IGNORECASE) for p in GREETING_PATTERNS)

def get_greeting_response(lang_code: str) -> str:
    return GREETING_RESPONSES.get(lang_code, GREETING_RESPONSES['en'])

# ──────────────────────────────────────────────
# META / IDENTITY QUESTIONS
# ──────────────────────────────────────────────
META_KEYWORDS = [
    # English
    'who are you', 'what are you', 'what is agroadvisor',
    'how were you built', 'how are you built', 'how do you work',
    'what data do you have', 'what can you do', 'your capabilities',
    'what sources', 'what documents', 'your knowledge base',
    'which model', 'what model', 'which ai', 'what ai',
    'who made you', 'who created you', 'who built you',
    'what is your purpose', 'introduce yourself',
    # Bengali script
    'তুমি কে', 'তুমি কী', 'আপনি কে', 'কে তুমি',
    'তোমার পরিচয়', 'তোমাকে কে বানিয়েছে',
    'তোমার কাছে কি তথ্য', 'কি ধরনের ডেটা',
    'তোমার ডেটাবেস', 'তুমি কিভাবে কাজ করো',
    'কোন মডেল', 'কোন এআই',
    # Romanized Bengali
    'tumi ke', 'tmi ke', 'apni ke', 'tomar porichoy',
    'ke tomake baniyeche', 'kibhabe kaj koro',
]

TECHNICAL_KEYWORDS = [
    'which model', 'what model', 'gpt', 'llama', 'groq',
    'openai', 'anthropic', 'which llm', 'what llm',
    'which ai model', 'technology stack', 'how were you built',
    'what technology', 'trained on', 'fine tuned',
]

META_ANSWER_EN = """I am **AgroAdvisor BD** 🌾, an AI agricultural assistant for Bangladesh.

**What I am:**
- A RAG (Retrieval-Augmented Generation) chatbot
- Built by a Bangladeshi AI/ML researcher
- Powered by a knowledge base of official agricultural documents

**My knowledge sources:**
- 🏛️ BRRI (Bangladesh Rice Research Institute)
- 🌾 IRRI (International Rice Research Institute)
- 🌍 FAO (Food and Agriculture Organization)
- 🔬 BARI (Bangladesh Agricultural Research Institute)
- 🇺🇸 USDA (US Department of Agriculture)
- 📚 AIS (Agriculture Information Service Bangladesh)

**I can help with:**
Crop diseases, pest management, rice/vegetable/fruit production, climate impacts, fertilizer use, and farming practices in Bangladesh."""

META_ANSWER_BN = """আমি **AgroAdvisor BD** 🌾 — বাংলাদেশের কৃষি বিষয়ক এআই সহকারী।

**আমি কী:**
- একটি RAG (Retrieval-Augmented Generation) চ্যাটবট
- একজন বাংলাদেশী AI/ML গবেষকের তৈরি
- সরকারি কৃষি ডকুমেন্ট থেকে তৈরি জ্ঞানভান্ডার ব্যবহার করি

**আমার তথ্যের উৎস:**
- 🏛️ BRRI (বাংলাদেশ ধান গবেষণা ইনস্টিটিউট)
- 🌾 IRRI (আন্তর্জাতিক ধান গবেষণা ইনস্টিটিউট)
- 🌍 FAO (জাতিসংঘ কৃষি সংস্থা)
- 🔬 BARI (বাংলাদেশ কৃষি গবেষণা ইনস্টিটিউট)
- 🇺🇸 USDA (আমেরিকান কৃষি বিভাগ)
- 📚 AIS (কৃষি তথ্য সার্ভিস, বাংলাদেশ)

**আমি যে বিষয়ে সাহায্য করতে পারি:**
ফসলের রোগ, পোকামাকড় দমন, ধান/সবজি/ফল উৎপাদন, জলবায়ু প্রভাব, সার ব্যবস্থাপনা।"""

TECHNICAL_ANSWER_EN = """**Technical details:**
- **LLM:** I use a large language model via the Groq API for fast inference
- **Embedding model:** paraphrase-multilingual-mpnet-base-v2 (handles Bengali + English)
- **Vector database:** ChromaDB for semantic search
- **Framework:** LangChain + Streamlit
- **Knowledge base:** ~10,000+ chunks from 32+ agricultural PDFs
- **Languages:** English and Bengali (বাংলা)

I was built as a portfolio/research project focused on agricultural AI for Bangladesh."""

TECHNICAL_ANSWER_BN = """**প্রযুক্তিগত বিবরণ:**
- **LLM:** Groq API-তে বড় ভাষা মডেল ব্যবহার করি
- **Embedding:** paraphrase-multilingual-mpnet-base-v2 (বাংলা + ইংরেজি সমর্থন করে)
- **Vector DB:** ChromaDB — সিম্যান্টিক সার্চের জন্য
- **ফ্রেমওয়ার্ক:** LangChain + Streamlit
- **জ্ঞানভান্ডার:** ৩২+ PDF থেকে ~১০,০০০+ চাংক
- **ভাষা:** বাংলা এবং ইংরেজি

এটি বাংলাদেশের কৃষি AI নিয়ে একটি গবেষণা ও পোর্টফোলিও প্রজেক্ট হিসেবে তৈরি।"""

def is_meta_question(query: str) -> bool:
    lower_q = query.lower()
    return any(kw in lower_q for kw in META_KEYWORDS)

def is_technical_question(query: str) -> bool:
    lower_q = query.lower()
    return any(kw in lower_q for kw in TECHNICAL_KEYWORDS)

def get_meta_answer(lang_code: str) -> str:
    return META_ANSWER_BN if lang_code == 'bn' else META_ANSWER_EN

def get_technical_answer(lang_code: str) -> str:
    return TECHNICAL_ANSWER_BN if lang_code == 'bn' else TECHNICAL_ANSWER_EN

# ──────────────────────────────────────────────
# SOURCE FORMATTING — clean ugly hash IDs
# ──────────────────────────────────────────────
UUID_PATTERN = re.compile(r'^[0-9a-f]{32}$', re.IGNORECASE)
HEX_PATTERN = re.compile(r'^[0-9a-f]{8,}$', re.IGNORECASE)

def is_valid_source_name(source: str) -> bool:
    """Filter out hash/UUID chunk IDs that look terrible."""
    s = source.replace('-', '').replace('_', '')
    if UUID_PATTERN.match(s):
        return False
    if HEX_PATTERN.match(s) and len(s) > 16:
        return False
    if len(source) < 4:
        return False
    return True

def clean_source_name(source: str) -> str:
    """Make source names readable."""
    name = source.replace('.pdf', '').replace('.txt', '')
    name = name.replace('_', ' ').replace('-', ' ')
    return name.title()

def format_retrieved_chunks(chunks: list) -> str:
    parts = []
    for i, chunk in enumerate(chunks, 1):
        source = chunk.source or "Unknown"
        sim = f"{chunk.similarity_score:.0%}" if chunk.similarity_score else "?"
        header = f"[Source {i}: {source} | Relevance: {sim}]"
        parts.append(f"{header}\n{chunk.text}")
    return "\n\n---\n\n".join(parts)

# ── Follow-up question patterns ──────────────────────────────
FOLLOWUP_PATTERNS = [
    r'^(r|ar|aro|আর|আরো|আরও)\s*(kichu|কিছু|bolo|বলো|bolun|বলুন)',
    r'^(eita|এইটা|eta|এটা)\s*(niye|নিয়ে|somporke|সম্পর্কে)',
    r'^(tell me more|more details|details please|explain more)',
    r'^(আরো বলো|আরো বলুন|বিস্তারিত বলো|আরও কিছু)',
    r'^(r\s*kichu|ar\s*kichu)',
]

def is_followup_question(query: str) -> bool:
    """Detect follow-up / continuation questions."""
    q = query.strip().lower()
    # Very short queries after a conversation are likely follow-ups
    if len(q.split()) <= 4 and len(q) < 30:
        return any(re.search(p, q, re.IGNORECASE) for p in FOLLOWUP_PATTERNS)
    return any(re.search(p, q, re.IGNORECASE) for p in FOLLOWUP_PATTERNS)