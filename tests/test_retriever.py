from src.retriever import retrieve_documents

def test_retrieve_documents():

    results = retrieve_documents(
        "credit card fraud",
        k=3
    )

    assert len(results) > 0