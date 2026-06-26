"""
evaluate.py — Fixed with proper JSON serialization
"""
import json
import numpy as np
from src.retrieval import load_vectorstore
from src.hybrid_retrieval import hybrid_retrieve, load_bm25_index
from src.generation import generate
from src.language import detect_language

# ── Updated eval dataset with flexible source matching ──
EVAL_DATASET = [
    {
        "query": "ধানের ব্লাস্ট রোগের লক্ষণ কী?",
        "expected_keywords": ["ব্লাস্ট", "দাগ", "সাদা", "পাতা", "blast"],
        "expected_sources": ["rice_diseases", "blast_threat", "rice_blast"],
        "language": "bn"
    },
    {
        "query": "ধানের ব্লাস্ট রোগে কোন ওষুধ ব্যবহার করতে হবে?",
        "expected_keywords": ["tricyclazole", "ট্রাইসাইক্লাজোল", "isoprothiolane",
                              "ছত্রাকনাশক", "fungicide", "স্প্রে"],
        "expected_sources": ["rice_diseases", "blast_threat", "rice_blast",
                              "brri_annual"],
        "language": "bn"
    },
    {
        "query": "বোরো ধানে কতটুকু ইউরিয়া সার দিতে হয়?",
        "expected_keywords": ["ইউরিয়া", "urea", "কেজি", "kg", "সার",
                              "fertilizer", "হেক্টর"],
        "expected_sources": ["fertilizer", "rice_production", "krishi_diary",
                              "brri"],
        "language": "bn"
    },
    {
        "query": "আলুর লেট ব্লাইট রোগের লক্ষণ ও প্রতিকার কী?",
        "expected_keywords": ["আলু", "ব্লাইট", "blight", "ম্যানকোজেব",
                              "mancozeb", "phytophthora", "ছত্রাক"],
        "expected_sources": ["potato", "late_blight", "purdue"],
        "language": "bn"
    },
    {
        "query": "What are the symptoms of rice blast disease?",
        "expected_keywords": ["blast", "lesion", "symptom", "leaf",
                              "neck", "white", "gray", "brown"],
        "expected_sources": ["rice_diseases", "blast_threat", "rice_blast",
                              "fao_rice", "irri"],
        "language": "en"
    },
    {
        "query": "What fungicide is used to control rice blast?",
        "expected_keywords": ["tricyclazole", "isoprothiolane", "fungicide",
                              "spray", "propiconazole"],
        "expected_sources": ["rice_diseases", "blast_threat", "brri_annual"],
        "language": "en"
    },
    {
        "query": "When did wheat blast first appear in Bangladesh?",
        "expected_keywords": ["2016", "wheat", "blast", "bangladesh",
                              "february", "district"],
        "expected_sources": ["wheat", "blast_threat", "wheat_blast",
                              "usda_wheat"],
        "language": "en"
    },
    {
        "query": "Which rice varieties are flood tolerant in Bangladesh?",
        "expected_keywords": ["BRRI", "dhan49", "dhan51", "dhan52",
                              "flood", "submergence", "tolerant"],
        "expected_sources": ["rice_varieties", "brri", "irri"],
        "language": "en"
    },
    {
        "query": "How does climate change affect rice production in Bangladesh?",
        "expected_keywords": ["climate", "temperature", "flood", "salinity",
                              "drought", "yield", "production"],
        "expected_sources": ["climate", "foresight", "iucn", "fao_bd"],
        "language": "en"
    },
    {
        "query": "What is the fertilizer recommendation for potato in Bangladesh?",
        "expected_keywords": ["urea", "TSP", "MoP", "potato", "fertilizer",
                              "kg", "hectare"],
        "expected_sources": ["potato", "fertilizer", "bari", "krishi"],
        "language": "en"
    },
]

def check_source_hit(chunks, expected_sources):
    """Flexible source matching — checks if ANY expected source
    is a substring of ANY retrieved source name."""
    all_sources = " ".join([c.source.lower() for c in chunks])
    for expected in expected_sources:
        if expected.lower() in all_sources:
            return True, expected
    return False, None

def check_keyword_hit(answer, expected_keywords):
    """Check if ANY expected keyword appears in the answer."""
    answer_lower = answer.lower()
    found = [kw for kw in expected_keywords if kw.lower() in answer_lower]
    return len(found) >= 1, found

# Custom JSON encoder to handle NumPy types
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.bool_):
            return bool(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

def evaluate():
    print("Loading vectorstore...")
    collection = load_vectorstore("data/faiss_db")

    # Try to load BM25
    bm25, corpus, metadatas = load_bm25_index()
    use_hybrid = bm25 is not None
    print(f"Using hybrid retrieval: {use_hybrid}")
    if not use_hybrid:
        print("WARNING: BM25 index not found. Run build_bm25.py first for better results.")
        from src.retrieval import retrieve as basic_retrieve

    results = []
    keyword_hits = 0
    source_hits = 0
    reliable_count = 0

    for i, item in enumerate(EVAL_DATASET):
        query = item["query"]
        expected_kw = item["expected_keywords"]
        expected_src = item["expected_sources"]
        lang = item["language"]

        # Retrieval
        if use_hybrid:
            chunks, has_reliable = hybrid_retrieve(query, collection, top_k=8)
        else:
            chunks, has_reliable = basic_retrieve(query, collection, top_k=8)

        # Generation
        answer, used_chunks = generate(query, chunks, has_reliable, lang)

        # Evaluation
        kw_hit, kw_found = check_keyword_hit(answer, expected_kw)
        src_hit, matched_src = check_source_hit(chunks, expected_src)

        if kw_hit:
            keyword_hits += 1
        if src_hit:
            source_hits += 1
        if has_reliable:
            reliable_count += 1

        # --- Convert all values to JSON‑serializable types ---
        result = {
            "query": query,
            "has_reliable": bool(has_reliable),
            "keyword_hit": bool(kw_hit),
            "source_hit": bool(src_hit),
            "keywords_found": [str(k) for k in kw_found],
            "matched_source": str(matched_src) if matched_src else None,
            "top_chunks": [
                {
                    "source": c.source,
                    "score": float(c.similarity_score),
                    "text_preview": c.text[:100]
                }
                for c in chunks[:3]
            ],
            "answer_preview": str(answer[:300])
        }
        results.append(result)

        status_kw = "✅" if kw_hit else "❌"
        status_src = "✅" if src_hit else "❌"
        print(f"\n[{i+1}/{len(EVAL_DATASET)}] {query[:55]}...")
        print(f"  Reliable: {'✅' if has_reliable else '❌'} | "
              f"Keywords: {status_kw} {kw_found[:2]} | "
              f"Source: {status_src} {matched_src}")
        if chunks:
            print(f"  Top score: {chunks[0].similarity_score:.3f} | "
                  f"Source: {chunks[0].source}")
        else:
            print("  No results")

    # Final report
    total = len(EVAL_DATASET)
    print(f"\n{'='*60}")
    print(f"EVALUATION RESULTS")
    print(f"{'='*60}")
    print(f"Total questions:      {total}")
    print(f"Keyword accuracy:     {keyword_hits}/{total} = {keyword_hits/total*100:.1f}%")
    print(f"Source accuracy:      {source_hits}/{total} = {source_hits/total*100:.1f}%")
    print(f"Reliable responses:   {reliable_count}/{total} = {reliable_count/total*100:.1f}%")
    avg_score = sum(
        r['top_chunks'][0]['score'] for r in results if r['top_chunks']
    ) / total
    print(f"Avg top similarity:   {avg_score:.3f}")

    # Grade
    kw_pct = keyword_hits / total * 100
    if kw_pct >= 80:
        grade = "🟢 EXCELLENT"
    elif kw_pct >= 60:
        grade = "🟡 GOOD — needs improvement"
    elif kw_pct >= 40:
        grade = "🟠 FAIR — significant gaps"
    else:
        grade = "🔴 POOR — major issues"
    print(f"\nOverall Grade: {grade}")

    # Problem diagnosis
    print(f"\n📋 DIAGNOSIS:")
    if avg_score < 0.5:
        print("  ⚠️  Low similarity scores — "
              "knowledge base content may not match query style")
        print("     Fix: Re-run build_complete_knowledge.py, "
              "then re-ingest")
    if source_hits / total < 0.5:
        print("  ⚠️  Low source accuracy — "
              "wrong chunks being retrieved")
        print("     Fix: Run diagnose.py to see actual source names, "
              "update eval dataset")
    if keyword_hits / total < 0.5:
        print("  ⚠️  Low keyword accuracy — "
              "LLM not using specific terms from context")
        print("     Fix: Strengthen system prompt, "
              "lower temperature, add few-shot examples")

    # Save detailed results with custom encoder
    try:
        with open("eval_results.json", "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2, cls=NumpyEncoder)
        print(f"\nDetailed results saved to eval_results.json")
    except Exception as e:
        print(f"⚠️  Could not save JSON: {e}")
        # Fallback: save as plain text
        with open("eval_results.txt", "w", encoding="utf-8") as f:
            f.write(str(results))

if __name__ == "__main__":
    evaluate()