from src.preprocess import clean_text

def test_clean_text():

    result = clean_text(
        "Hello!!! World 123"
    )

    assert result == "hello world"
