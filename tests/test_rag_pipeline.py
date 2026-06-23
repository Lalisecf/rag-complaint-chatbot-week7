from src.retriever import retrieve_documents

def test_rag_components():

    docs = retrieve_documents(
        "credit card fraud",
        k=5
    )

    assert len(docs) == 5