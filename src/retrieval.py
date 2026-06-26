import chromadb
from sentence_transformers import SentenceTransformer, CrossEncoder
from dataclasses import dataclass
from collections import defaultdict

# ── Config ─────────────────────────────────────────────────
EMBEDDING_MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
RELEVANCE_THRESHOLD = 0.45
MAX_CHUNKS_PER_SOURCE = 2
CHROMA_DIR = "data/faiss_db"

_model = None
_cross_encoder = None


def get_model():
    global _model
    if _model is None:
        print("Loading embedding model...")
        _model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        print("Model loaded.")
    return _model


def get_cross_encoder():
    global _cross_encoder
    if _cross_encoder is None:
        print("Loading cross-encoder...")
        _cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
        print("Cross-encoder loaded.")
    return _cross_encoder


def load_vectorstore(chroma_dir: str = CHROMA_DIR):
    """
    Load ChromaDB collection using the new PersistentClient API.
    Raises an error if the collection does not exist.
    """
    try:
        client = chromadb.PersistentClient(path=chroma_dir)
        collection = client.get_collection("agricultural_knowledge")
        print(f"ChromaDB loaded — Total chunks: {collection.count()}")
        return collection
    except Exception as e:
        raise RuntimeError(
            f"Failed to load ChromaDB from '{chroma_dir}'. "
            f"Make sure the directory exists and contains a valid collection. "
            f"Original error: {e}"
        )

# alias for backward compatibility
load_collection = load_vectorstore


@dataclass
class RetrievedChunk:
    text: str
    source: str
    chunk_id: int
    similarity_score: float
    page: int = None


def is_garbage_chunk(text: str) -> bool:
    stripped = text.strip()
    if len(stripped) < 120:
        return True
    alpha_ratio = sum(c.isalpha() for c in stripped) / max(len(stripped), 1)
    if alpha_ratio < 0.4:
        return True
    if stripped.startswith("[Page") and len(stripped) < 30:
        return True
    return False


def diversify_sources(chunks: list, max_per_source: int = MAX_CHUNKS_PER_SOURCE) -> list:
    source_counts = defaultdict(int)
    diversified = []
    for chunk in chunks:
        src = chunk.source
        if source_counts[src] < max_per_source:
            diversified.append(chunk)
            source_counts[src] += 1
    return diversified


def rerank_chunks(query: str, chunks: list, top_k: int = 5) -> list:
    if not chunks:
        return []
    model = get_cross_encoder()
    pairs = [[query, chunk.text] for chunk in chunks]
    scores = model.predict(pairs)
    scored = sorted(zip(chunks, scores), key=lambda x: x[1], reverse=True)
    return [item[0] for item in scored[:top_k]]


def retrieve(query: str, collection, top_k: int = 10) -> tuple:
    model = get_model()
    query_embedding = model.encode(query, normalize_embeddings=True).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    raw_chunks = []
    for i in range(len(results["documents"][0])):
        distance = results["distances"][0][i]
        similarity = round(1 - distance, 4)
        text = results["documents"][0][i]
        meta = results["metadatas"][0][i]

        chunk = RetrievedChunk(
            text=text,
            source=meta.get("source", "Unknown"),
            chunk_id=meta.get("chunk_id", 0),
            similarity_score=similarity,
            page=meta.get("page")
        )
        raw_chunks.append(chunk)

    clean_chunks = [c for c in raw_chunks if not is_garbage_chunk(c.text)]
    relevant_chunks = [c for c in clean_chunks if c.similarity_score >= RELEVANCE_THRESHOLD]
    diverse_chunks = diversify_sources(relevant_chunks, max_per_source=MAX_CHUNKS_PER_SOURCE)
    reranked = rerank_chunks(query, diverse_chunks, top_k=5)

    has_reliable = len(reranked) > 0
    return reranked, has_reliable