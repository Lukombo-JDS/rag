from langchain_core.vectorstores import VectorStore
from langchain_text_splitters.spacy import SpacyTextSplitter
from langchain_core.documents import Document
from scripts.var import *


# Adding embed chunks to vector store

def embeddingContents(docs: list[Document], vectorStore: VectorStore):
    print("DOCS: ", docs[:2])
    print("DOCS size: ", len(docs))
    _ = vectorStore.add_documents(docs)

def chunking(contents: list[Document]) -> list[Document]:

    splitter = SpacyTextSplitter(
        separator="\n\n",
        chunk_overlap=SPLITTER_CHUNKS_OVERLAP,
        chunk_size=SPLITTER_CHUNKS,
        max_length=SPACY_SPLITTER_MAX_LENGTH
        )

    return splitter.split_documents(contents)


def injestion(contents: list[Document], vectorStore: VectorStore):
    chunked = chunking(contents)

    embeddingContents(chunked, vectorStore)