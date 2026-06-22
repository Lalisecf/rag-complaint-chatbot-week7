import pandas as pd

from chunking import chunk_text
from embedding import generate_embeddings
from vector_store import create_collection


def main():

    try:

        df = pd.read_csv(
            "data/processed/filtered_complaints.csv"
        )

    except FileNotFoundError:

        print("Filtered dataset not found")
        return

    if df.empty:

        print("Dataset is empty")
        return

    chunks = []

    for idx, row in df.iterrows():

        for chunk in chunk_text(
            row["clean_text"]
        ):

            chunks.append({
                "id": str(len(chunks)),
                "text": chunk,
                "product": row["Product"]
            })

    texts = [
        c["text"]
        for c in chunks
    ]

    embeddings = generate_embeddings(texts)

    collection = create_collection()

    for i, chunk in enumerate(chunks):

        collection.add(
            ids=[chunk["id"]],
            documents=[chunk["text"]],
            embeddings=[
                embeddings[i].tolist()
            ],
            metadatas=[{
                "product":
                chunk["product"]
            }]
        )

    print(
        f"Indexed {len(chunks)} chunks"
    )


if __name__ == "__main__":
    main()