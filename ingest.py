from src.ingestion import build_vectorstore
from src.hybrid_retrieval import build_bm25_index
from src.retrieval import load_vectorstore

if __name__ == "__main__":
    # Step 1 — Build vector store
    build_vectorstore(
        pdf_dir="data/all_documents",
        save_dir="data/faiss_db"
    )

    # Step 2 — Build BM25 index
    print("\nBuilding BM25 index...")
    collection = load_vectorstore("data/faiss_db")
    build_bm25_index(collection, save_path="data/bm25_index.pkl")
    print("BM25 index built successfully.")