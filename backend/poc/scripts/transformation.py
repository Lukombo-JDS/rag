from langchain_core.vectorstores import VectorStore
from langchain_text_splitters.spacy import SpacyTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from scripts.var import *
from typing import Iterable
from scripts.extraction import extractContents


# chunking logic 

def chunk_logic(page_token_size:int, nb_size:int, device_capacity):
    pass


def chunking(contents: Iterable[Document]) -> list[Document]:

    # print("pre-chunking-docs: ", contents[:1])

    splitter = RecursiveCharacterTextSplitter(
            chunk_size=SPLITTER_CHUNKS,
            chunk_overlap=SPLITTER_CHUNKS_OVERLAP,
            separators=["\n\n"]
        )

    return splitter.split_documents(contents)


def transformation(docs_path: str)->list[Document]:
    return chunking(
        extractContents(docs_path)
    )