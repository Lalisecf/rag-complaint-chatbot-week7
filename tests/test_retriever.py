from src.retriever import retrieve_documents

def test_retriever():

    docs = retrieve_documents(
        "credit card complaint"
    )

    assert len(docs) > 0
