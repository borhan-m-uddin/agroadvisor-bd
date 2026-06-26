import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from dataclasses import dataclass
from typing import List
import pickle
import os

EMBEDDING_MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
RELEVANCE_THRESHOLD = 0.35
BM25_WEIGHT = 0.3       # weight for keyword search
DENSE_WEIGHT = 0.7      # weight for semantic search

_model = None
_bm25_index = None
_bm25_corpus = None     # all chunk texts
_bm25_metadata = None   # all chunk metadata

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return _model

def build_bm25_index(collection, save_path="data/bm25_index.pkl"):
    """Build BM25 index from ChromaDB — fetches in batches to avoid SQL limit."""
    print("Building BM25 index...")

    total = collection.count()
    print(f"Total chunks to index: {total}")

    all_documents = []
    all_metadatas = []

    # Fetch in batches of 5000
    BATCH_SIZE = 5000
    offset = 0

    while offset < total:
        batch_size = min(BATCH_SIZE, total - offset)
        print(f"  Fetching batch {offset}-{offset + batch_size}...")

        try:
            results = collection.get(
                include=["documents", "metadatas"],
                limit=batch_size,
                offset=offset
            )
            all_documents.extend(results["documents"])
            all_metadatas.extend(results["metadatas"])
            offset += batch_size
        except Exception as e:
            print(f"  Batch error at offset {offset}: {e}")
            # Try smaller batch
            BATCH_SIZE = BATCH_SIZE // 2
            if BATCH_SIZE < 100:
                print("  Batch size too small, stopping")
                break
            continue

    print(f"  Fetched {len(all_documents)} documents total")

    # Build BM25 index
    print("  Tokenizing and building index...")
    tokenized = [doc.lower().split() for doc in all_documents]
    bm25 = BM25Okapi(tokenized)

    # Save to disk
    os.makedirs(os.path.dirname(save_path) if os.path.dirname(save_path) else ".", exist_ok=True)
    with open(save_path, "wb") as f:
        pickle.dump({
            "bm25": bm25,
            "documents": all_documents,
            "metadatas": all_metadatas
        }, f)

    size_mb = os.path.getsize(save_path) / (1024 * 1024)
    print(f"BM25 index built — {len(all_documents)} documents")
    print(f"Saved to {save_path} ({size_mb:.1f} MB)")
    return bm25, all_documents, all_metadatas

def load_bm25_index(save_path="data/bm25_index.pkl"):
    global _bm25_index, _bm25_corpus, _bm25_metadata
    if _bm25_index is None:
        if not os.path.exists(save_path):
            return None, None, None
        with open(save_path, "rb") as f:
            data = pickle.load(f)
        _bm25_index = data["bm25"]
        _bm25_corpus = data["documents"]
        _bm25_metadata = data["metadatas"]
    return _bm25_index, _bm25_corpus, _bm25_metadata

@dataclass
class RetrievedChunk:
    text: str
    source: str
    chunk_id: int
    similarity_score: float
    page: int = None

def hybrid_retrieve(query: str, collection, top_k: int = 8) -> tuple:
    """
    Hybrid search combining dense vector + BM25 keyword search.
    Returns merged and deduplicated results.
    """
    model = get_model()

    # ── Dense retrieval ──────────────────────────────
    query_embedding = model.encode(query, normalize_embeddings=True).tolist()
    dense_results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    dense_chunks = {}
    for i in range(len(dense_results["documents"][0])):
        text = dense_results["documents"][0][i]
        distance = dense_results["distances"][0][i]
        similarity = (1 - distance) * DENSE_WEIGHT
        meta = dense_results["metadatas"][0][i]
        dense_chunks[text[:100]] = {
            "text": text,
            "source": meta.get("source", "Unknown"),
            "chunk_id": meta.get("chunk_id", 0),
            "page": meta.get("page"),
            "score": similarity
        }

    # ── BM25 keyword retrieval ────────────────────────
    bm25, corpus, metadatas = load_bm25_index()

    if bm25 is not None:
        tokenized_query = query.lower().split()
        bm25_scores = bm25.get_scores(tokenized_query)
        top_bm25_indices = np.argsort(bm25_scores)[::-1][:top_k]

        # Normalize BM25 scores to 0-1
        max_score = bm25_scores[top_bm25_indices[0]] if bm25_scores[top_bm25_indices[0]] > 0 else 1
        for idx in top_bm25_indices:
            if bm25_scores[idx] <= 0:
                continue
            text = corpus[idx]
            normalized_score = (bm25_scores[idx] / max_score) * BM25_WEIGHT
            key = text[:100]
            if key in dense_chunks:
                # Boost score if found by both methods
                dense_chunks[key]["score"] += normalized_score
            else:
                meta = metadatas[idx] if idx < len(metadatas) else {}
                dense_chunks[key] = {
                    "text": text,
                    "source": meta.get("source", "Unknown"),
                    "chunk_id": meta.get("chunk_id", 0),
                    "page": meta.get("page"),
                    "score": normalized_score
                }

    # ── Sort by combined score ────────────────────────
    sorted_chunks = sorted(
        dense_chunks.values(),
        key=lambda x: x["score"],
        reverse=True
    )[:top_k]

    chunks = [
        RetrievedChunk(
            text=c["text"],
            source=c["source"],
            chunk_id=c["chunk_id"],
            similarity_score=round(c["score"], 4),
            page=c["page"]
        )
        for c in sorted_chunks
    ]

    has_reliable = len(chunks) > 0 and chunks[0].similarity_score >= RELEVANCE_THRESHOLD
    return chunks, has_reliable