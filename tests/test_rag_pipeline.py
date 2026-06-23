from src.rag_pipeline import answer_question

def test_rag():

    result = answer_question(
        "Why are customers unhappy with credit cards?"
    )

    assert "answer" in result