import hashlib
import json
import os
import time

CACHE_FILE = "data/response_cache.json"
CACHE_TTL = 7 * 24 * 3600  # 1 week in seconds

def _load_cache() -> dict:
    if not os.path.exists(CACHE_FILE):
        return {}
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_cache(cache: dict):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def cache_key(query: str, lang: str) -> str:
    normalized = query.lower().strip()
    return hashlib.md5(f"{normalized}_{lang}".encode()).hexdigest()

def get_cached(query: str, lang: str):
    cache = _load_cache()
    key = cache_key(query, lang)
    if key in cache:
        entry = cache[key]
        if time.time() - entry["timestamp"] < CACHE_TTL:
            print(f"Cache hit for: {query[:50]}")
            return entry["answer"]
    return None

def set_cached(query: str, lang: str, answer: str):
    cache = _load_cache()
    key = cache_key(query, lang)
    cache[key] = {
        "query": query,
        "answer": answer,
        "timestamp": time.time()
    }
    # Keep only last 500 entries
    if len(cache) > 500:
        oldest_keys = sorted(cache, key=lambda k: cache[k]["timestamp"])[:100]
        for k in oldest_keys:
            del cache[k]
    _save_cache(cache)