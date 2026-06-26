from src.retrieval import load_collection, retrieve

print("Loading database...")
collection = load_collection("data/faiss_db")   # adjust if your ChromaDB path is different

test_queries = [
    "What are the symptoms of rice blast disease?",
    "How to manage sheath blight in Bangladesh?",
    "ধানের ব্লাস্ট রোগের লক্ষণ কী?",
    "What is wheat blast and when did it appear in Bangladesh?",
    "How does climate affect crop disease in Bangladesh?",
    "What fungicide is used for rice blast?",
    "Symptoms of bacterial leaf blight in rice",
]

print(f"\nRunning {len(test_queries)} test queries...\n")
print("=" * 60)

for query in test_queries:
    print(f"\nQUERY: {query}")
    chunks, has_reliable = retrieve(query, collection, top_k=8)  # fetch 8, re‑rank to top 5
    print(f"Reliable: {has_reliable}")
    if chunks:
        for i, c in enumerate(chunks):
            page_info = f" | Page {c.page}" if c.page else ""
            print(f"  [{i+1}] Score: {c.similarity_score:.3f} | Source: {c.source}{page_info}")
            print(f"       {c.text[:150]}...")
    else:
        print("  No results returned")
    print("-" * 40)