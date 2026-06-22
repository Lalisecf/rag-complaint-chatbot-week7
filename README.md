# Intelligent Complaint Analysis for Financial Services
## Week 7 Challenge – Interim Submission (Task 1 & Task 2)

### 10 Academy – Artificial Intelligence Mastery Program

---

## Project Overview

CrediTrust Financial is a rapidly growing digital financial services provider operating across East Africa. The company receives thousands of customer complaints every month regarding products such as Credit Cards, Personal Loans, Savings Accounts, and Money Transfers.

The objective of this project is to build the foundation of a Retrieval-Augmented Generation (RAG) system that enables internal stakeholders to query customer complaints using natural language and obtain evidence-based insights.

This interim submission covers:

- Task 1: Exploratory Data Analysis (EDA) and Data Preprocessing
- Task 2: Text Chunking, Embedding Generation, and Vector Store Construction

---

## Business Objective

The project aims to transform unstructured customer complaints into actionable insights by:

- Identifying major complaint trends faster
- Empowering non-technical teams to access complaint information
- Supporting proactive issue identification and decision-making

---

## Dataset

Source: Consumer Financial Protection Bureau (CFPB)

The dataset contains:

- Consumer complaint narratives
- Product information
- Company information
- Issue and sub-issue categories
- Complaint metadata

For this challenge, only complaints related to the following product categories were retained:

1. Credit Cards
2. Personal Loans
3. Savings Accounts
4. Money Transfers

---

## Project Structure

```text
rag-complaint-chatbot/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── task1_eda.ipynb
│
├── src/
│
├── vector_store/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Task 1: Exploratory Data Analysis & Preprocessing

## Objectives

- Understand the structure of complaint data
- Analyze complaint distribution
- Investigate narrative quality
- Clean and prepare text for semantic search

---

## EDA Activities

### Product Distribution Analysis

The distribution of complaints across product categories was analyzed to understand data imbalance and representation.

### Narrative Length Analysis

Consumer complaint narrative lengths were measured using word counts to identify:

- Extremely short complaints
- Extremely long complaints
- Average complaint length

Visualizations were created to better understand narrative distributions.

### Missing Narrative Analysis

Complaints with missing consumer narratives were identified and quantified.

---

## Data Filtering

The dataset was filtered to retain only the following products:

- Credit Card
- Personal Loan
- Savings Account
- Money Transfer

Records with missing or empty narratives were removed.

---

## Text Cleaning

The following preprocessing steps were applied:

- Conversion to lowercase
- Removal of special characters
- Removal of punctuation
- Removal of boilerplate phrases
- Whitespace normalization

---

## Output

Generated dataset:

```text
data/processed/filtered_complaints.csv
```

---

# Task 2: Text Chunking, Embedding & Vector Store Construction

## Objectives

Prepare complaint narratives for semantic search and retrieval.

---

## Sampling Strategy

A stratified sampling approach was used to create a representative subset of complaints.

Characteristics:

- Approximately 10,000–15,000 complaints
- Preserves proportional representation of each product category
- Ensures balanced semantic coverage

---

## Text Chunking

Long complaint narratives were split into smaller chunks using:

```python
RecursiveCharacterTextSplitter
```

Configuration:

```python
chunk_size = 500
chunk_overlap = 50
```

### Justification

- Preserves semantic meaning
- Improves retrieval quality
- Reduces embedding information loss
- Maintains context continuity between chunks

---

## Embedding Model

Model used:

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Why This Model?

- Lightweight and efficient
- Produces high-quality sentence embeddings
- Widely used in semantic search systems
- Generates 384-dimensional embeddings
- Recommended in challenge resources

---

## Embedding Generation

Each text chunk was converted into a dense vector representation using Sentence Transformers.

Output:

```python
embeddings = model.encode(
    chunks,
    show_progress_bar=True
)
```

---

## Vector Database

Vector Store:

```text
ChromaDB
```

Stored information:

- Chunk text
- Complaint ID
- Product Category
- Embedding Vector

The vector store is persisted in:

```text
vector_store/
```

---

## Deliverables Completed

### Task 1

- [x] EDA Notebook
- [x] Product Distribution Analysis
- [x] Narrative Length Analysis
- [x] Missing Narrative Analysis
- [x] Data Filtering
- [x] Text Cleaning
- [x] Filtered Dataset Export

### Task 2

- [x] Stratified Sampling
- [x] Text Chunking
- [x] Embedding Generation
- [x] ChromaDB Index Construction
- [x] Vector Store Persistence

---

## Technologies Used

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Machine Learning & NLP

- Sentence Transformers
- LangChain

### Vector Database

- ChromaDB

### Development Environment

- Python 3.11+
- Jupyter Notebook

---

## Reproducing Results

### Clone Repository

```bash
git clone https://github.com/<username>/rag-complaint-chatbot.git
cd rag-complaint-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run EDA Notebook

```bash
jupyter notebook notebooks/task1_eda.ipynb
```

---

## Challenges Encountered

- Large complaint dataset size
- High computational cost of embedding generation
- Product imbalance across complaint categories
- Long narrative handling and chunk optimization

---

## Next Steps

### Task 3

- Build Retrieval Pipeline
- Implement Similarity Search
- Design Prompt Template
- Integrate Large Language Model
- Evaluate RAG Performance

### Task 4

- Build Interactive Gradio Interface
- Display Retrieved Sources
- Improve User Experience
- Deploy End-to-End RAG Application

---

## Author

**Lalise Fufi**

10 Academy – Artificial Intelligence Mastery Program

Week 7 Challenge

Intelligent Complaint Analysis for Financial Services