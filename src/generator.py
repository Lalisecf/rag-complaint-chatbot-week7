from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=256
)

def generate_answer(prompt):

    result = generator(prompt)

    return result[0]["generated_text"]