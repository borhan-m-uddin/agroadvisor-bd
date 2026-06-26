# diagnose.py
from src.retrieval import load_vectorstore, retrieve

collection = load_vectorstore("data/faiss_db")

print(f"Total chunks: {collection.count()}")
print("\n=== CHECKING ACTUAL SOURCE NAMES ===")

# Get sample of all unique sources
results = collection.get(include=["metadatas"], limit=500)
sources = set()
for meta in results["metadatas"]:
    sources.add(meta.get("source", "unknown"))

print(f"\nUnique sources found ({len(sources)} total):")
for s in sorted(sources):
    print(f"  {s}")

print("\n=== TESTING RETRIEVAL FOR EACH EVAL QUERY ===")
test_queries = [
    "ধানের ব্লাস্ট রোগের লক্ষণ কী?",
    "ধানের ব্লাস্ট রোগে কোন ওষুধ দিতে হবে?",
    "বোরো ধানে কতটুকু ইউরিয়া সার দিতে হয়?",
    "আলুর লেট ব্লাইট রোগ কী?",
    "What are symptoms of rice blast disease?",
    "What fungicide is recommended for rice blast?",
    "When did wheat blast first appear in Bangladesh?",
    "What are flood tolerant rice varieties?",
]

for query in test_queries:
    chunks, reliable = retrieve(query, collection, top_k=3)
    print(f"\nQ: {query[:60]}")
    print(f"   Reliable: {reliable}")
    for i, c in enumerate(chunks):
        print(f"   [{i+1}] score={c.similarity_score:.3f} | source={c.source}")
        print(f"        text={c.text[:120]}...")