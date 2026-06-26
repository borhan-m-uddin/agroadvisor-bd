# build_bm25.py
from src.retrieval import load_vectorstore
from src.hybrid_retrieval import build_bm25_index

print("Loading ChromaDB...")
collection = load_vectorstore("data/faiss_db")

print(f"Building BM25 index for {collection.count()} chunks...")
build_bm25_index(collection, save_path="data/bm25_index.pkl")
print("Done!")