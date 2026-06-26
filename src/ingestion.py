import os
import re
from pathlib import Path
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
import fitz  # PyMuPDF
from tqdm import tqdm

# ----------------------------------------------------------------------
# 1. Embedding model (cached)
# ----------------------------------------------------------------------
EMBEDDING_MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
_model = None

def get_model():
    """Load and cache the SentenceTransformer model."""
    global _model
    if _model is None:
        print("Loading embedding model (first time only, ~30 seconds)...")
        _model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return _model

# ----------------------------------------------------------------------
# 2. Text extraction from PDF and TXT
# ----------------------------------------------------------------------
def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract clean text from a PDF file."""
    doc = fitz.open(pdf_path)
    pages_text = []
    for page_num, page in enumerate(doc):
        text = page.get_text("text")
        # Clean up common PDF artifacts
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' {2,}', ' ', text)
        text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)
        text = text.strip()
        if len(text) > 50:
            pages_text.append(f"[Page {page_num + 1}]\n{text}")
    doc.close()
    return "\n\n".join(pages_text)

def extract_text_from_txt(txt_path: str) -> str:
    """Read plain text files (scraped content)."""
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"  TXT read error: {e}")
        return ""

# ----------------------------------------------------------------------
# 3. Chunking
# ----------------------------------------------------------------------
def create_chunks(text: str, source_name: str) -> list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    raw_chunks = splitter.split_text(text)
    chunks = []
    for i, chunk in enumerate(raw_chunks):
        chunk = chunk.strip()
        if len(chunk) < 100:
            continue

        # Extract page number
        page_num = 0  # default to 0 instead of None
        if chunk.startswith("[Page") and "]" in chunk:
            try:
                page_num = int(chunk.split("[Page")[1].split("]")[0].strip())
            except Exception:
                page_num = 0

        chunks.append({
            "text": chunk,
            "metadata": {
                "source": str(source_name),        # ensure string
                "chunk_id": int(i),                # ensure int
                "total_chunks": int(len(raw_chunks)), # ensure int
                "page": int(page_num)              # ensure int, never None
            }
        })
    return chunks
# ----------------------------------------------------------------------
# 4. Generate embeddings in batches
# ----------------------------------------------------------------------
def generate_embeddings(chunks: list, batch_size: int = 32) -> list:
    """Generate embeddings for a list of chunks."""
    model = get_model()
    texts = [c["text"] for c in chunks]
    all_embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        embeddings = model.encode(
            batch,
            normalize_embeddings=True,
            show_progress_bar=False
        )
        all_embeddings.extend(embeddings.tolist())
    return all_embeddings

# ----------------------------------------------------------------------
# 5. ChromaDB setup and storage
# ----------------------------------------------------------------------
def setup_chromadb(persist_directory: str):
    """Create or open a ChromaDB persistent client and collection."""
    client = chromadb.PersistentClient(
        path=persist_directory,
        settings=Settings(anonymized_telemetry=False)
    )
    collection = client.get_or_create_collection(
        name="agricultural_knowledge",
        metadata={"hnsw:space": "cosine"}
    )
    return client, collection

def store_chunks(collection, chunks: list, embeddings: list, source_name: str):
    ids = []
    for i, chunk in enumerate(chunks):
        raw_id = f"{source_name}_{chunk['metadata']['chunk_id']}"
        clean_id = re.sub(r'[^a-zA-Z0-9_-]', '_', raw_id)[:100]
        ids.append(clean_id)

    texts = [c["text"] for c in chunks]

    # Sanitize all metadata — ChromaDB only accepts str, int, float, bool
    sanitized_metadatas = []
    for c in chunks:
        clean_meta = {}
        for key, value in c["metadata"].items():
            if value is None:
                clean_meta[key] = ""        # None string → empty string
            elif isinstance(value, (str, int, float, bool)):
                clean_meta[key] = value     # already valid
            else:
                clean_meta[key] = str(value) # convert anything else to string
        sanitized_metadatas.append(clean_meta)

    batch_size = 500
    for i in range(0, len(ids), batch_size):
        collection.add(
            ids=ids[i:i+batch_size],
            embeddings=embeddings[i:i+batch_size],
            documents=texts[i:i+batch_size],
            metadatas=sanitized_metadatas[i:i+batch_size]
        )

# ----------------------------------------------------------------------
# 6. Main build function (ChromaDB)
# ----------------------------------------------------------------------
def build_vectorstore(pdf_dir: str = "pdfs", save_dir: str = "chroma_db"):
    os.makedirs(save_dir, exist_ok=True)

    pdf_files = sorted(Path(pdf_dir).glob("**/*.pdf"))
    txt_files = sorted(Path(pdf_dir).glob("**/*.txt"))
    all_files = pdf_files + txt_files

    print(f"Found {len(pdf_files)} PDFs + {len(txt_files)} text files\n")

    client, collection = setup_chromadb(save_dir)
    failed = []
    total_chunks = 0

    for file_path in tqdm(all_files, desc="Processing files"):
        # ── Clean source name: use filename only, no path ──
        source_name = file_path.stem  # just filename without extension
        print(f"\nProcessing: {file_path.name} → source: {source_name}")

        try:
            if file_path.suffix == '.pdf':
                text = extract_text_from_pdf(str(file_path))
            else:
                text = extract_text_from_txt(str(file_path))

            if len(text.strip()) < 200:
                print(f"  SKIPPED — too little text ({len(text)} chars)")
                failed.append(file_path.name)
                continue

            chunks = create_chunks(text, source_name)
            if not chunks:
                print(f"  SKIPPED — no chunks")
                failed.append(file_path.name)
                continue

            embeddings = generate_embeddings(chunks)
            store_chunks(collection, chunks, embeddings, source_name)
            total_chunks += len(chunks)
            print(f"  ✅ {len(chunks)} chunks stored. Total: {total_chunks}")

        except Exception as e:
            print(f"  ❌ ERROR: {e}")
            failed.append(file_path.name)

    print(f"\n✅ Ingestion complete. Total: {total_chunks} chunks")
    if failed:
        print(f"Failed: {failed}")