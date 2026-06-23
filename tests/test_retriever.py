import faiss
from pathlib import Path

INDEX_PATH = Path("vector_store/faiss_index.bin")


def load_index():

    if not INDEX_PATH.exists():
        raise FileNotFoundError(
            f"{INDEX_PATH} not found"
        )

    return faiss.read_index(str(INDEX_PATH))


def retrieve_documents(query, k=5):

    index = load_index()

    # retrieval logic here

    return []