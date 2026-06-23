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

    # Optional: use a smaller dataset for faster testing
    # df = df.head(10000)

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

    print(f"Total chunks: {len(chunks)}")

    texts = [
        c["text"]
        for c in chunks
    ]

    print("Generating embeddings...")

    embeddings = generate_embeddings(texts)

    print(
        f"Embeddings generated: {len(embeddings)}"
    )

    collection = create_collection()

    BATCH_SIZE = 500

    for start in range(
        0,
        len(chunks),
        BATCH_SIZE
    ):

        end = min(
            start + BATCH_SIZE,
            len(chunks)
        )

        collection.add(
            ids=[
                c["id"]
                for c in chunks[start:end]
            ],
            documents=[
                c["text"]
                for c in chunks[start:end]
            ],
            embeddings=[
                embeddings[i].tolist()
                for i in range(start, end)
            ],
            metadatas=[
                {
                    "product": c["product"]
                }
                for c in chunks[start:end]
            ]
        )

        print(
            f"Inserted {end}/{len(chunks)}"
        )

    print(
        f"Indexed {len(chunks)} chunks"
    )


if __name__ == "__main__":
    main()