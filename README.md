# PixieSupportAI 🌸

PixieSupportAI is an AI-powered customer support assistant built with **Python, Streamlit, LangChain, Ollama, ChromaDB, and SQLite**. It uses **Retrieval-Augmented Generation (RAG)** to answer customer queries, track orders, and create support tickets using a local LLM.

---

## Features

- AI-powered customer support chatbot
- Retrieval-Augmented Generation (RAG)
- Local LLM using Ollama (Qwen 2.5)
- Order tracking system
- Support ticket creation
- SQLite database integration
- ChromaDB vector database
- Streamlit web interface

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Ollama
- Qwen 2.5
- ChromaDB
- SQLite
- HuggingFace Embeddings

---

## Project Structure

```text
PixieSupportAI/
│── app.py
│── ingest.py
│── graph.py
│── agent.py
│── tools.py
│── database.py
│── support.db
│── requirements.txt
│── README.md
│
├── chroma_db/
├── data/
└── images/
```

---

## Architecture

```text
              User
                │
                ▼
         Streamlit UI
                │
                ▼
        PixieSupportAI
                │
      ┌─────────┼─────────┐
      ▼         ▼         ▼
  Order DB   Ticket DB    RAG
      │         │          │
      └─────────┼──────────┘
                ▼
          Ollama (Qwen)
```

---

## Installation

```bash
git clone https://github.com/your-username/PixieSupportAI.git

cd PixieSupportAI

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

ollama serve

ollama pull qwen2.5:0.5b

python ingest.py

streamlit run app.py
```

---

## Screenshots

| Home | Order Tracking |
|------|----------------|
| *(Add Screenshot)* | *(Add Screenshot)* |

| Ticket Creation | AI Chat |
|-----------------|---------|
| *(Add Screenshot)* | *(Add Screenshot)* |

---

## Future Enhancements

- User authentication
- Login & registration
- Chat history
- Admin dashboard
- Multi-language support

---

## Author

**Preethi Kumari**

Bachelor of Engineering – Information Science & Engineering

GitHub: https://github.com/your-username



---

If you found this project useful, consider giving it a ⭐ on GitHub.
