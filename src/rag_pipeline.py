from src.retriever import retrieve_documents
from src.generator import generate_answer
from src.prompt_template import PROMPT_TEMPLATE


def answer_question(question):

  
    docs = retrieve_documents(
    question,
    k=10
    )

    context = "\n\n".join(
        [d["document"] for d in docs]
    )

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    answer = generate_answer(prompt)

    return {
        "answer": answer,
        "sources": docs
    }