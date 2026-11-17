# Traditional RAG – Data Ingestion Pipeline

**A foundational Retrieval-Augmented Generation (RAG) implementation using Python, LangChain, Hugging Face Embeddings and ChromaDB.**

## 1. Project Overview

This project implements the data ingestion component of a Traditional RAG pipeline. It demonstrates how unstructured PDF documents can be processed, transformed into vector embeddings and stored in a vector database to prepare them for semantic retrieval.

The project uses an Organic Farming PDF document as the sample knowledge source.

## 2. Project Scope

The implementation covers four stages of the RAG data ingestion process:

| Stage | Scope |
|---|---|
| Document Loading | Extract text and metadata from PDF documents using PyPDFLoader. |
| Text Chunking | Divide extracted content into smaller, overlapping chunks using RecursiveCharacterTextSplitter. |
| Embedding Generation | Convert text chunks into numerical vector representations using Hugging Face embeddings. |
| Vector Storage | Store document chunks, embeddings and metadata in ChromaDB for future retrieval. |

**Current milestone:** Traditional RAG – Data Ingestion.

Semantic retrieval and LLM-based answer generation are outside the scope of this milestone.

## 3. Technology Stack

| Technology | Implementation Purpose |
|---|---|
| Python | Pipeline development |
| LangChain | Document processing and integration |
| PyPDFLoader | PDF document ingestion |
| RecursiveCharacterTextSplitter | Text chunking |
| Hugging Face Sentence Transformers | Embedding generation |
| all-MiniLM-L6-v2 | Embedding model |
| ChromaDB | Vector database |

## 4. Implementation and Validation

The pipeline was implemented and validated using a sample PDF document.

| Component | Implementation / Result |
|---|---|
| Source document | Organic Farming PDF |
| Total pages processed | 3 |
| Chunking strategy | 1,000 characters with 200-character overlap |
| Total chunks generated | 13 |
| Embedding model | all-MiniLM-L6-v2 |
| Embedding dimensions | 384 |
| Embeddings generated | 13 |
| Vector database | ChromaDB |
| Records stored | 13 |

The implementation also validates the stored document content and associated metadata.

## 5. Architecture and Project Implementation

**Data ingestion workflow:**

PDF Document → Document Loading → Text Chunking → Embedding Generation → ChromaDB Vector Storage

**Source Code Structure**

```text
traditional-rag-data-ingestion/
│
├── src/
│   ├── data_loader.py
│   ├── text_chunker.py
│   ├── embedding_generator.py
│   └── vector_store.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

**Future Development:** Extend the ingestion pipeline with semantic similarity search, relevant document retrieval and LLM-based answer generation to build an end-to-end RAG application.

---

**Project Type:** AI / Generative AI Portfolio Project  
**Implementation:** Traditional RAG – Data Ingestion Pipeline