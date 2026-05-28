# Document RAG Assistant

An AI-powered document question-answering system built using Python and FastAPI.

This project implements a Retrieval Augmented Generation (RAG) pipeline where users can upload documents and ask natural language questions. The system retrieves relevant document context using semantic search and generates grounded responses using an LLM.

---

# Features

* Upload PDF documents
* Extract and process document text
* Chunk large documents into smaller contexts
* Generate vector embeddings
* Store embeddings in a vector database
* Semantic similarity search
* LLM-powered contextual responses
* FastAPI-based REST APIs
* Swagger/OpenAPI documentation
* Modular and scalable backend architecture

---

# Tech Stack

## Backend

* Python
* FastAPI
* Uvicorn

## AI / NLP

* LangChain
* OpenAI API
* Sentence Transformers

## Vector Search

* FAISS

## Document Processing

* PyPDF

## Future Enhancements

* MongoDB
* Redis
* Docker
* Async background workers
* Authentication and authorization
* Streaming responses
* Multi-document conversations

---

# Project Structure

```text
document-rag/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── vectorstore/
│
├── tests/
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/
```

---

# System Architecture

```text
User
  ↓
FastAPI API Layer
  ↓
Document Upload Service
  ↓
PDF Extraction
  ↓
Text Chunking
  ↓
Embedding Generation
  ↓
FAISS Vector Store
  ↓
Semantic Retrieval
  ↓
LLM Response Generation
```

---

# API Flow

## Document Upload

```text
Upload PDF
→ Extract Text
→ Chunk Document
→ Generate Embeddings
→ Store Vectors
```

## Chat Flow

```text
User Question
→ Generate Query Embedding
→ Semantic Similarity Search
→ Retrieve Relevant Chunks
→ Send Context + Question to LLM
→ Generate Response
```

---

# Getting Started

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

---

# Swagger API Docs

```text
http://127.0.0.1:8000/docs
```

---

# Current Development Status

## Phase 1

* [x] FastAPI setup
* [x] Project structure
* [x] Virtual environment setup

## Upcoming

* [ ] PDF upload API
* [ ] PDF text extraction
* [ ] Text chunking
* [ ] Embedding generation
* [ ] Vector storage
* [ ] Semantic search
* [ ] OpenAI integration
* [ ] Conversation memory
* [ ] Dockerization
* [ ] Production deployment

---

# Learning Goals

This project is designed to explore:

* AI application engineering
* Retrieval Augmented Generation (RAG)
* Vector databases
* Semantic search
* LLM orchestration
* FastAPI backend development
* Scalable AI system design

---

# Author

Built as part of a hands-on AI engineering and backend systems learning journey.
