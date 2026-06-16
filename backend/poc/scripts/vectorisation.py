from langchain_core.vectorstores import VectorStore
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

# Adding embed chunks to vector store

def embeddingContents(docs: list[Document], vectorStore: VectorStore)->VectorStore:
    _ = vectorStore.add_documents(docs)


def embeddingRequest(request: str, embeder: Embeddings) -> list[float]:
    return embeder.embed_query(request)