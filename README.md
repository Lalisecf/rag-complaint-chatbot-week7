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
git clone https://github.com/<your-username>/rag-complaint-chatbot.git
cd rag-complaint-chatbot
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
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

# Future Work

## Task 3

* Semantic Retriever Implementation
* Similarity Search Optimization
* Prompt Engineering
* LLM Integration
* RAG Evaluation

## Task 4

* Gradio User Interface
* Source Citation Display
* End-to-End Chatbot Integration
* Deployment

---

# Author

**Lalise Fufi**

10 Academy – Artificial Intelligence Mastery Program

Week 7 Challenge – Intelligent Complaint Analysis for Financial Services
