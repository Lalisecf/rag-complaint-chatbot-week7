# Intelligent Complaint Analysis for Financial Services

## Week 7 Challenge – Interim Submission (Task 1 & Task 2)

### 10 Academy – Artificial Intelligence Mastery Program

---

## Project Overview

CrediTrust Financial receives millions of customer complaints across multiple financial products. These complaints contain valuable insights into customer experiences, service issues, fraud concerns, and operational challenges.

The goal of this project is to build the foundation of a Retrieval-Augmented Generation (RAG) system that enables stakeholders to query customer complaints using natural language and receive evidence-based answers supported by complaint narratives.

This interim submission covers:

* Task 1: Exploratory Data Analysis (EDA) and Data Preprocessing
* Task 2: Text Chunking, Embedding Generation, and Vector Store Construction

---

## Repository Structure

```text
rag-complaint-chatbot-week7/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── filtered_complaints.csv
│
├── notebooks/
│   └── task1_eda.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── chunking.py
│   ├── embedding.py
│   ├── vector_store.py
│   └── build_vector_store.py
│
├── tests/
│   └── test_preprocess.py
│
├── vector_store/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Task 1: Exploratory Data Analysis & Data Preprocessing

## Objectives

* Explore complaint distributions across products
* Analyze narrative quality and completeness
* Investigate narrative length characteristics
* Clean and prepare complaint narratives for retrieval tasks

## Dataset Overview

Source: CFPB Consumer Complaint Database

### Initial Dataset Statistics

| Metric                       | Value     |
| ---------------------------- | --------- |
| Total Complaints             | 9,609,797 |
| Number of Features           | 18        |
| Missing Narratives           | 6,629,041 |
| Missing Narrative Percentage | 68.98%    |

## Data Preprocessing Pipeline

The preprocessing workflow includes:

* Filtering target products
* Removing empty complaint narratives
* Lowercasing text
* Removing special characters
* Removing unnecessary whitespace
* Cleaning boilerplate text

Implemented in:

```text
src/preprocess.py
```

### Output

```text
data/processed/filtered_complaints.csv
```

---

# Task 2: Text Chunking, Embedding, and Vector Store Construction

## Objectives

Prepare complaint narratives for semantic retrieval and future RAG integration.

## Sampling Strategy

A stratified sampling approach was applied to preserve representation across product categories while reducing computational cost.

Target sample size:

```text
10,000 – 15,000 complaints
```

## Text Chunking

Implemented in:

```text
src/chunking.py
```

Method:

```python
RecursiveCharacterTextSplitter
```

Configuration:

```python
chunk_size = 500
chunk_overlap = 50
```

### Why Chunking?

* Preserves semantic context
* Improves retrieval quality
* Reduces information loss
* Supports efficient embedding generation

## Embedding Generation

Implemented in:

```text
src/embedding.py
```

Embedding Model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Model Benefits

* Lightweight and efficient
* Generates 384-dimensional embeddings
* Suitable for semantic similarity search
* Widely used in RAG systems

## Vector Store Construction

Implemented in:

```text
src/vector_store.py
src/build_vector_store.py
```

Vector Database:

```text
ChromaDB
```

Stored Metadata:

* Complaint ID
* Product Category
* Complaint Chunk Text
* Embedding Vector

Persisted Location:

```text
vector_store/
```

---

# Running the Project

## 1. Clone Repository

```bash
git clone https://github.com/<lalisecf>/rag-complaint-chatbot-week7.git
cd rag-complaint-chatbot-week7
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Task 1

Run the notebook:

```bash
jupyter notebook notebooks/task1_eda.ipynb
```

Or execute preprocessing module:

```bash
python src/preprocess.py
```

---

# Running Task 2

Build embeddings and vector database:

```bash
python src/build_vector_store.py
```

The script:

1. Loads filtered complaint data
2. Performs chunking
3. Generates embeddings
4. Creates ChromaDB collection
5. Stores chunks and metadata
6. Persists the vector index

---

# Testing

Basic unit tests are included.

Run:

```bash
pytest tests/
```

Example test:

```text
tests/test_preprocess.py
```

---

# Error Handling

Basic robustness checks have been added to the pipeline:

* Missing file detection
* Empty dataset validation
* Safe text preprocessing
* Collection creation safeguards

These checks improve reliability and make the codebase easier to extend in later tasks.

---

# Deliverables Completed

## Task 1

* [x] Exploratory Data Analysis
* [x] Product Distribution Analysis
* [x] Narrative Length Analysis
* [x] Missing Narrative Analysis
* [x] Product Filtering
* [x] Text Cleaning
* [x] Filtered Dataset Export

## Task 2

* [x] Stratified Sampling
* [x] Text Chunking Module
* [x] Embedding Generation Module
* [x] ChromaDB Vector Store Module
* [x] End-to-End Vector Store Pipeline
* [x] Persistent Vector Index

---

# Challenges Encountered

* Large-scale CFPB dataset processing
* High percentage of missing narratives
* Product category imbalance
* Embedding generation computational cost
* Chunk size optimization for retrieval performance

---

## Updated Repository Structure

```text
rag-complaint-chatbot-week7/
│
├── data/
│   ├── raw/
│   │   └── complaint_embeddings.parquet
│   └── processed/
│       └── filtered_complaints.csv
│
├── notebooks/
│   ├── task1_eda.ipynb
│   ├── task3_rag_evaluation.ipynb
│   └── task4_demo.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── chunking.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── build_vector_store.py
│   ├── create_faiss_index.py
│   ├── retriever.py
│   ├── generator.py
│   ├── prompt_template.py
│   ├── rag_pipeline.py
│   └── __init__.py
│
├── tests/
│   ├── test_preprocess.py
│   ├── test_retriever.py
│   ├── test_rag_pipeline.py
│   └── __init__.py
│
├── vector_store/
│   ├── faiss_index.bin
│   ├── documents.pkl
│   └── metadata.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Task 3: Retrieval-Augmented Generation (RAG)

## Objectives

Build a semantic retrieval system capable of:

* Retrieving relevant complaint narratives
* Providing context-aware answers
* Supporting evidence-based decision making
* Serving as the backend for an intelligent complaint chatbot

## Retrieval Architecture

### Embedding Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Vector Search Engine

```text
FAISS (Facebook AI Similarity Search)
```

### Language Model

```text
google/flan-t5-base
```

## Components

### Retriever

Implemented in:

```text
src/retriever.py
```

Responsibilities:

* Load FAISS index
* Encode user query
* Perform similarity search
* Retrieve top-k complaint chunks
* Return complaint metadata

### Generator

Implemented in:

```text
src/generator.py
```

Responsibilities:

* Construct prompts
* Generate natural-language answers
* Ground responses using retrieved context

### RAG Pipeline

Implemented in:

```text
src/rag_pipeline.py
```

Pipeline Flow:

```text
User Question
      ↓
Query Embedding
      ↓
FAISS Retrieval
      ↓
Top-K Complaint Chunks
      ↓
Prompt Construction
      ↓
FLAN-T5 Generation
      ↓
Final Answer + Sources
```

## Evaluation Results

| Question                                                  | Interpretation                                                                 | Score |
| --------------------------------------------------------- | ------------------------------------------------------------------------------ | ----- |
| Why are customers unhappy with credit cards?              | Relevant answer but based on a specific complaint rather than a broad summary. | 3.5/5 |
| What fraud issues are common?                             | Strong retrieval of fraud-related complaints and identity theft concerns.      | 4.0/5 |
| What billing disputes occur most often?                   | Accurately identified unauthorized charges and billing errors.                 | 4.5/5 |
| Why do customers complain about money transfers?          | Weak retrieval due to limited representation in indexed subset.                | 2.0/5 |
| What issues are reported for personal loans?              | Strong answer highlighting payment and credit reporting problems.              | 4.5/5 |
| What credit card problems do customers report most often? | Relevant but focused on one complaint theme.                                   | 3.5/5 |
| What fraud complaints are common among credit card users? | Very strong retrieval with multiple fraud scenarios represented.               | 4.5/5 |
| Why do customers dispute credit card charges?             | Correctly identified unauthorized purchases and refund issues.                 | 4.0/5 |
| What problems occur when making loan payments?            | Strong retrieval and accurate answer generation.                               | 4.5/5 |
| How do credit reporting issues affect customers?          | Relevant answer regarding credit score damage and reporting inaccuracies.      | 4.5/5 |

### Task 3 Summary

The RAG system successfully retrieves semantically similar complaint narratives and generates evidence-based answers grounded in complaint data. Performance was strongest for Credit Card and Personal Loan complaint categories.

---

# Task 4: Interactive Chatbot Interface

## Objectives

Develop a user-friendly interface allowing stakeholders to interact with the complaint knowledge base using natural language.

## Framework

```text
Gradio
```

Implemented in:

```text
app.py
```

## Features

### Natural Language Question Input

Users can ask questions such as:

```text
What fraud complaints are common among credit card users?
```

### AI-Generated Answers

Responses are generated using the Retrieval-Augmented Generation pipeline.

### Source Transparency

The chatbot displays:

* Complaint ID
* Product Category
* Company Name
* Complaint Issue
* Complaint Excerpt

This improves explainability and trustworthiness.

### Interactive Components

* Question Textbox
* Ask Button
* AI Answer Panel
* Retrieved Sources Panel
* Clear Button

## System Workflow

```text
User Question
      ↓
Retriever
      ↓
FAISS Similarity Search
      ↓
Top Complaint Chunks
      ↓
FLAN-T5 Generator
      ↓
Answer Generation
      ↓
Display Sources
```

---

# Running Task 3

```bash
python src/create_faiss_index.py
```

Evaluate the RAG pipeline:

```bash
jupyter notebook notebooks/task3_rag_evaluation.ipynb
```

---

# Running Task 4

Launch the chatbot:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:7860
```

---

# Deliverables Completed

## Task 1

* [x] Exploratory Data Analysis
* [x] Narrative Cleaning
* [x] Product Filtering
* [x] Missing Value Analysis

## Task 2

* [x] Chunking Pipeline
* [x] Embedding Generation
* [x] Vector Store Construction
* [x] Metadata Storage

## Task 3

* [x] FAISS Index Creation
* [x] Semantic Retrieval
* [x] Prompt Engineering
* [x] FLAN-T5 Integration
* [x] RAG Evaluation

## Task 4

* [x] Gradio User Interface
* [x] Answer Generation
* [x] Source Citation Display
* [x] Interactive Chatbot
* [x] End-to-End RAG System

---

# Challenges Encountered

* Processing large-scale CFPB complaint data
* Memory limitations when loading full complaint embeddings
* FAISS index construction on limited hardware
* Context length limitations of FLAN-T5
* Retrieval quality variations across product categories

---

# Future Improvements

* Index the full complaint embedding dataset
* Improve retrieval ranking strategies
* Implement reranking models
* Add conversation memory
* Deploy chatbot to cloud infrastructure
* Support advanced analytics dashboards


---

# Author

**Lalise Fufi**

10 Academy – Artificial Intelligence Mastery Program

Week 7 Challenge – Intelligent Complaint Analysis for Financial Services
