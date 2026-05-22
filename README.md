# 🧠 Local LLM with RAG — Django + Ollama

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![Ollama](https://img.shields.io/badge/Ollama-Llama3-orange)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue)

A fully local LLM system with RAG (Retrieval-Augmented Generation) pipeline built with **Django**, **Ollama**, **ChromaDB**, and **MySQL**. No external API calls — everything runs on your own machine.

## 🏗️ Architecture

```
User Query
    ↓
Django REST API
    ↓
Query Embedding (sentence-transformers)
    ↓
Vector Search (ChromaDB / FAISS)
    ↓
Top-K Relevant Chunks fetched
    ↓
[Context + Query] → Local LLM (Ollama/Llama3)
    ↓
Response saved to MySQL
    ↓
Returned to User
```

## ✨ Features

- 🏠 100% local — no OpenAI/Anthropic API needed
- 📄 Ingest PDFs, text files, and websites
- 🔍 Semantic search with ChromaDB vector store
- 💬 Chat with memory stored in MySQL
- 🌐 Web scraping for knowledge base expansion
- ⚙️ Celery async tasks for ingestion

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Web Framework | Django 4.x + DRF |
| Local LLM | Ollama (Llama 3.2) |
| Embeddings | sentence-transformers |
| Vector Store | ChromaDB |
| Database | MySQL 8.0 |
| Task Queue | Celery + Redis |
| Web Scraping | BeautifulSoup4 |

## 🚀 Quick Start

```bash
# 1. Install Ollama and pull model
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull llama3.2

# 2. Clone and setup
git clone https://github.com/rashedkhanrubel-spec/local-llm-rag-django
cd local-llm-rag-django
pip install -r requirements.txt
cp .env.example .env

# 3. Setup database and run
python manage.py migrate
python manage.py runserver
```

## 📬 Contact

Built by [Md Rashed Khan](https://www.freelancer.com/u/rashedkhanrubel) — Available for AI & automation projects.

