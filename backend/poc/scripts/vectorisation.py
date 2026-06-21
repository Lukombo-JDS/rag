import numpy as np
import ollama
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore
from numpy.typing import NDArray

# Adding embed chunks to vector store

# Adding embeding chunks into vector store


def embeddingContents(
    docs: list[Document], vectorStore: VectorStore, embeder: Embeddings
) -> VectorStore:

    try:
        e = embeder
        return vectorStore.from_documents(documents=docs, embedding=e)

    except Exception as err:
        print(err)
        exit()


def embeddingRequest(request: str, embeder: Embeddings) -> list[float]:
    return embeder.embed_query(request)

def normalization(embeddings: list[list[float]] | list[float]) -> list[list[float]]:

    embed: NDArray = np.array(embeddings)

    norms: NDArray = np.linalg.norm(embed, axis=1, keepdims=True)

    normed_embeddings = embeddings / norms

    return normed_embeddings.tolist()


def check_vec_norm(model_name: str) -> bool:

    res = ollama.embed(
        model=model_name,
        input="Un test pour avoir la dimension des vecteurs du model"
    )

    vec = res["embeddings"][0]

    norm = np.linalg.norm(vec)

    if abs(norm - 1.0) >= 1e-6:
        return False
    return True
