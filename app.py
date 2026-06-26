import streamlit as st
from src.retrieval import load_vectorstore, retrieve
from src.hybrid_retrieval import hybrid_retrieve
from src.generation import generate, rewrite_query
from src.language import detect_language
from src.cache import get_cached, set_cached

# ── Page config ──────────────────────────────
st.set_page_config(
    page_title="AgroAdvisor BD",
    page_icon="🌾",
    layout="wide"
)

# ── Load vectorstore once at startup ─────────
@st.cache_resource
def get_vectorstore():
    return load_vectorstore("data/faiss_db")

vectorstore = get_vectorstore()

# ── Session state init ────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_sources" not in st.session_state:
    st.session_state.last_sources = []

# ── Sidebar ───────────────────────────────────
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2889/2889676.png", width=80)
    st.title("🌾 AgroAdvisor BD")
    st.markdown("Agricultural Disease Advisory for Bangladesh")
    st.markdown("---")

    try:
        chunk_count = vectorstore.count()
        st.metric("Knowledge Base", f"{chunk_count:,} chunks")
    except Exception:
        st.metric("Knowledge Base", "N/A")

    st.markdown("**Languages:** 🇬🇧 English | 🇧🇩 বাংলা")
    st.markdown("**Sources:** BRRI, IRRI, FAO, BARI, USDA, AIS")
    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.last_sources = []
        st.rerun()

    if st.session_state.last_sources:
        st.markdown("### 📄 Sources Used")
        seen = set()
        for chunk in st.session_state.last_sources:
            if chunk.source not in seen:
                seen.add(chunk.source)
                display = chunk.source.replace(".pdf", "").replace("_", " ").title()
                st.markdown(f"- **{display}** ({chunk.similarity_score:.0%})")

# ── Main area ─────────────────────────────────
st.title("🌾 Agricultural Disease Advisory Chatbot")
st.markdown("Ask me anything about crop diseases, symptoms, treatments, and prevention in Bangladesh.")

with st.expander("📝 Example questions to try"):
    st.markdown("""
    - What are the symptoms of rice blast disease?
    - How do I treat sheath blight in rice?
    - What caused the wheat blast outbreak in Bangladesh?
    - ধানের ব্লাস্ট রোগের লক্ষণ কী?
    - আলুর লেট ব্লাইট রোগ কীভাবে দমন করব?
    - How does temperature affect disease spread in rice?
    - What fungicide is recommended for rice blast?
    - সরিষার রোগ দমনে কী করব?
    """)

# ── Display chat history ───────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Chat input ────────────────────────────────
if prompt := st.chat_input("Ask about crop diseases... (English or Bengali)"):

    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):

            lang = detect_language(prompt)
            history = st.session_state.messages[:-1]

            # ── Check cache first ──────────────────
            cached = get_cached(prompt, lang)
            if cached:
                answer = cached
                used_chunks = []
                chunks = []
            else:
                # ── Rewrite ambiguous queries ──────
                try:
                    search_query = rewrite_query(prompt, history, lang)
                except Exception:
                    search_query = prompt

                # ── Hybrid retrieval ───────────────
                try:
                    chunks, has_reliable = hybrid_retrieve(
                        search_query, vectorstore, top_k=8
                    )
                except Exception:
                    chunks, has_reliable = retrieve(
                        search_query, vectorstore, top_k=8
                    )

                # ── Generate answer ────────────────
                answer, used_chunks = generate(
                    query=prompt,
                    chunks=chunks,
                    has_reliable=has_reliable,
                    lang_code=lang,
                    chat_history=history
                )

                # ── Save to cache ──────────────────
                set_cached(prompt, lang, answer)

        st.markdown(answer)

        # ── Show retrieved context ─────────────────
        if chunks:
            with st.expander("🔍 View retrieved context", expanded=False):
                for i, chunk in enumerate(chunks):
                    if chunk.similarity_score >= 0.6:
                        color = "🟢"
                    elif chunk.similarity_score >= 0.35:
                        color = "🟡"
                    else:
                        color = "🔴"
                    st.markdown(
                        f"{color} **Chunk {i+1}** — "
                        f"`{chunk.source}` | Score: `{chunk.similarity_score:.3f}`"
                    )
                    st.text(
                        chunk.text[:300] + "..."
                        if len(chunk.text) > 300
                        else chunk.text
                    )
                    st.markdown("---")

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.session_state.last_sources = used_chunks
    st.rerun()