from typing import TypedDict

from langchain_core.documents.base import Document
from langchain_core.embeddings.embeddings import Embeddings
from langchain_core.language_models.llms import LLM
from langchain_core.runnables import chain
from langchain_core.vectorstores import VectorStore
from langchain_milvus import Milvus
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_pymupdf4llm.pymupdf4llm_loader import PyMuPDF4LLMLoader
from langchain_text_splitters.spacy import SpacyTextSplitter

# Get Documnets


def extractContents(path: str = "../data/rich-dad-poor-dad.pdf"):
    return iter(PyMuPDF4LLMLoader(file_path=path).lazy_load())


# Chunking of documents content


def chunking(contents: list[Document]) -> list[Document]:

    splitter = SpacyTextSplitter(max_length=1024)

    return splitter.split_documents(contents)


# Init Vectore Store


def initMilvus(embeder: Embeddings):

    URI = "./milvus_example.db"

    return Milvus(
        embedding_function=embeder,
        connection_args={"uri": URI},
        index_params={"index_type": "FLAT", "metric_type": "COSINE"},
        drop_old=True,
    )


def EmbedModel():
    return OllamaEmbeddings(model="nomic-embed-text", base_url="http://localhost:11434")


# Adding embed chunks to vector store


def embeddingContents(docs: list[Document], vectorStore: Milvus):
    _ = vectorStore.add_documents(docs)


def embeddingReqest(request: str, embeder: Embeddings) -> list[float]:
    return embeder.embed_query(request)


def initLLM():
    return OllamaLLM(
        base_url="http://localhost:11434", model="qwen3:4b", temperature=0.35
    )


# Pipeline of the workflow of the RAG


class PipelineInputs(TypedDict):
    request: str
    vectorStore: VectorStore
    llm: OllamaLLM
    embedder: Embeddings


@chain
def retrievePipeline(inputs: PipelineInputs):
    request: str = inputs["request"]
    vectorStore: VectorStore = inputs["vectorStore"]
    llm: OllamaLLM = inputs["llm"]
    embedder: Embeddings = inputs["embedder"]

    embeddedRequest = embedder.embed_query(request)

    results = vectorStore.similarity_search_by_vector(
        embedding=embeddedRequest,
        k=4,
    )

    context = "\n\n".join(doc.page_content for doc in results)

    prompt = f"""
You have to exactly answer the given question:
{request}

With the given context:
{context}

Your answer:
"""

    for chunk in llm.stream(prompt):
        yield chunk


def output(request: str):

    inputs: PipelineInputs = {
        "request": request,
        "embedder": EmbedModel(),
        "vectorStore": initMilvus(EmbedModel()),
        "llm": initLLM(),
    }
    print("Hello from poc!")
    print("Vector DB ready !")

    return retrievePipeline.stream(inputs)
