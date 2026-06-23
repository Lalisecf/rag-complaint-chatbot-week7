import gradio as gr

from src.rag_pipeline import answer_question


def ask(question):

    result = answer_question(question)

    source_text = ""

    for item in result["sources"][:3]:

        meta = item["metadata"]

        source_text += f"""
Complaint ID: {meta['complaint_id']}
Product: {meta['product_category']}
Company: {meta['company']}
Issue: {meta['issue']}

Excerpt:
{item['document'][:300]}

--------------------------------------------------
"""

    return result["answer"], source_text


with gr.Blocks() as demo:

    gr.Markdown(
        "# CrediTrust Complaint Analysis Chatbot"
    )

    question = gr.Textbox(
        label="Ask a question"
    )

    ask_btn = gr.Button("Ask")

    answer = gr.Textbox(
        label="AI Answer"
    )

    sources = gr.Textbox(
        label="Retrieved Sources",
        lines=15
    )

    clear_btn = gr.ClearButton()

    ask_btn.click(
        ask,
        inputs=question,
        outputs=[
            answer,
            sources
        ]
    )

demo.launch()