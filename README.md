# 🌾 AgroAdvisor BD — Agricultural Disease Advisory Chatbot

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Spaces-Live-green)](https://borhan72-agroadvisor-bd.hf.space/)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue)](https://github.com/borhan-m-uddin/agroadvisor-bd)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-FF4B4B)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)

A bilingual (English/Bengali) RAG (Retrieval-Augmented Generation) chatbot for crop disease management, pest control, and agricultural advisory in Bangladesh.

**🌐 Live Demo:** [https://borhan72-agroadvisor-bd.hf.space/](https://borhan72-agroadvisor-bd.hf.space/)  
**📂 GitHub Repository:** [https://github.com/borhan-m-uddin/agroadvisor-bd](https://github.com/borhan-m-uddin/agroadvisor-bd)

---

## 📌 Overview

AgroAdvisor BD is an intelligent agricultural assistant that helps farmers, researchers, and agricultural extension officers in Bangladesh get instant answers about crop diseases, pest management, fertilizer recommendations, and climate impact on agriculture. The chatbot leverages a comprehensive knowledge base built from authoritative sources including BRRI, IRRI, FAO, BARI, USDA, and AIS publications.

It uses a **hybrid search** (vector + BM25) to retrieve the most relevant information and generates answers using state‑of‑the‑art language models (Hugging Face Inference API with Groq fallback). Responses are provided in the same language as the user's query (English or Bengali) with proper source citations.

---

## ✨ Features

- **🌾 Crop Disease Management** – Identify and manage diseases like rice blast, sheath blight, bacterial leaf blight, and wheat blast.
- **🧪 Fertilizer Recommendations** – Get site‑specific fertilizer advice for various crops including rice, potato, wheat, and vegetables.
- **🐛 Pest Management** – Integrated pest management (IPM) guidance for common agricultural pests in Bangladesh.
- **🌡️ Climate Impact** – Information on how climate change, temperature, and weather patterns affect crop production.
- **🌐 Bilingual Support** – Responds naturally in **English** or **Bengali (বাংলা)** based on user input.
- **📚 Source Citations** – Every answer includes references to the exact document and page number used.
- **🔍 Hybrid Search** – Combines vector similarity (ChromaDB) with BM25 keyword search for better retrieval.
- **🔄 Context‑Aware** – Maintains conversation history to handle follow‑up questions seamlessly.
- **⚡ Automatic Model Fallback** – If one LLM service is rate‑limited, it automatically switches to a backup model.

---

## 🧠 Knowledge Base

The chatbot is powered by a curated knowledge base of **30,000+ vector embeddings** from:

| Source | Type | Content |
|--------|------|---------|
| **BRRI** | Research Reports | Rice production, disease management, variety development |
| **IRRI** | Technical Manuals | Rice cultivation, pest control, nutrient management |
| **FAO** | Reports & Handbooks | Food security, biodiversity, crop production guides |
| **BARI** | Handbooks | Agricultural technology, crop varieties |
| **USDA** | Country Reports | Grain/food reports, oilseeds, fertilizer situation |
| **AIS** | Magazines & Articles | Krishi Kotha, e‑books, agricultural news |

**Total Documents:** 64 PDFs + 34 text files = **98 documents**  
**Total Chunks:** ~24,000 vector embeddings  
**Languages:** Bengali & English

---

## 🏗️ System Architecture

┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                         │
│                      (Streamlit Web App)                       │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Query Processing                        │
│  • Language Detection (Bengali / English)                      │
│  • Query Rewriting (with chat history)                         │
│  • Hybrid Retrieval (Vector + BM25)                           │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                         Knowledge Base                         │
│  ┌─────────────────────┐     ┌─────────────────────┐          │
│  │      ChromaDB       │     │      BM25 Index     │          │
│  │   (Vector Store)    │     │   (Keyword Store)   │          │
│  └─────────────────────┘     └─────────────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                        LLM Generation                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Primary: Hugging Face Inference API (Qwen2.5-7B)      │   │
│  │  Fallback: Groq API (Qwen3-32B / Llama3-70B)           │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Response Output                         │
│  • Natural language answers                                    │
│  • Source citations (document + page)                          │
│  • Bilingual (English / Bengali)                               │
│  • Bullet points for readability                               │
└─────────────────────────────────────────────────────────────────┘


---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Framework** | Streamlit 1.38.0 |
| **Vector Database** | ChromaDB 1.5.9 |
| **Embedding Model** | `sentence-transformers` (paraphrase‑multilingual‑mpnet‑base‑v2) |
| **LLM (Primary)** | Hugging Face Inference API (`Qwen/Qwen2.5-7B-Instruct`) |
| **LLM (Fallback)** | Groq API (`Qwen3-32B`, `Llama3-70B`) |
| **Search** | Hybrid (FAISS + BM25) |
| **PDF Processing** | PyMuPDF (fitz) |
| **Language** | Python 3.12 |
| **Deployment** | Hugging Face Spaces |

---

