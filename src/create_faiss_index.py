import pyarrow.parquet as pq
import pandas as pd

pf = pq.ParquetFile(
    "data/raw/complaint_embeddings.parquet"
)

chunks = []

for batch in pf.iter_batches(batch_size=10000):

    df = batch.to_pandas()

    chunks.append(df)

    if len(chunks) >= 10:
        break

df = pd.concat(chunks)

print(df.shape)

import numpy as np
import faiss
import pickle

embeddings = np.array(
    df["embedding"].tolist(),
    dtype=np.float32
)

print("Embeddings shape:", embeddings.shape)

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(embeddings)

faiss.write_index(
    index,
    "vector_store/faiss_index.bin"
)

with open(
    "vector_store/documents.pkl",
    "wb"
) as f:
    pickle.dump(
        df["document"].tolist(),
        f
    )

with open(
    "vector_store/metadata.pkl",
    "wb"
) as f:
    pickle.dump(
        df["metadata"].tolist(),
        f
    )

print("FAISS index saved successfully.")