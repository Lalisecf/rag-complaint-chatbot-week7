import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

index = faiss.read_index(
    str(BASE_DIR / "vector_store" / "faiss_index.bin")
)

with open(
    BASE_DIR / "vector_store" / "documents.pkl",
    "rb"
) as f:
    documents = pickle.load(f)

with open(
    BASE_DIR / "vector_store" / "metadata.pkl",
    "rb"
) as f:
    metadata = pickle.load(f)


def retrieve_documents(query, k=5):

    query_embedding = model.encode(
        [query]
    ).astype(np.float32)

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for idx in indices[0]:
        results.append({
            "document": documents[idx],
            "metadata": metadata[idx]
        })

    return results