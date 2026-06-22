import chromadb

def create_collection():

    client = chromadb.PersistentClient(
        path="vector_store"
    )

    return client.get_or_create_collection(
        "complaints"
    )