from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

db = Chroma(
    persist_directory="vector_store",
    embedding_function=embeddings
)

def retrieve_documents(query, k=5):
    docs = db.similarity_search(query, k=k)
    return docs