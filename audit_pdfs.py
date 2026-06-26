import os
import re
from pathlib import Path
import fitz  # PyMuPDF

# ------------------------------
# Configuration
# ------------------------------
PDF_DIR = "data/all_documents"  # root folder to scan recursively
MIN_WORDS = 200             # minimum word count to consider usable

def count_words(text: str) -> int:
    """Rough word count (Bengali + English)."""
    # Split by whitespace and count non‑empty tokens
    return len(re.findall(r'\S+', text))

def audit_pdf(pdf_path: str):
    """Extract page count and total words from a PDF."""
    try:
        doc = fitz.open(pdf_path)
        page_count = len(doc)
        full_text = ""
        for page in doc:
            full_text += page.get_text("text")
        doc.close()
        word_count = count_words(full_text)
        return page_count, word_count
    except Exception as e:
        return 0, 0

def audit_all_pdfs(root_dir: str):
    """Walk through root_dir recursively and audit every PDF."""
    root = Path(root_dir)
    if not root.exists():
        print(f"Directory not found: {root_dir}")
        return

    pdf_files = list(root.rglob("*.pdf"))   # recursive search
    if not pdf_files:
        print("No PDF files found.")
        return

    total = 0
    usable = 0
    skipped = 0

    print(f"{'File':<50} {'Pages':>6} {'Words':>10} Status")
    print("-" * 80)

    for pdf_path in sorted(pdf_files):
        rel_path = pdf_path.relative_to(root)
        pages, words = audit_pdf(str(pdf_path))

        total += 1
        if pages == 0 or words < MIN_WORDS:
            status = "SKIPPED (scanned/empty)"
            skipped += 1
        else:
            status = "OK"
            usable += 1

        # Display with nice formatting (truncate long names)
        name = str(rel_path)
        if len(name) > 45:
            name = "..." + name[-42:]
        print(f"{name:<50} {pages:>6} {words:>10,} {status}")

    # Summary
    print("\n" + "=" * 80)
    print(f"Total PDFs checked: {total}")
    print(f"Usable PDFs:        {usable}")
    print(f"Skipped (scanned/empty): {skipped}")

if __name__ == "__main__":
    audit_all_pdfs(PDF_DIR)