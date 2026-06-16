from langchain_core.embeddings.embeddings import Embeddings
from langchain_ollama.llms import OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_milvus import Milvus
from pymilvus import MilvusClient
from typing import TypedDict
from langchain_core.vectorstores import VectorStore, VectorStoreRetriever
from scripts.var import *

# Initialisation:
# BDD Vectorielle,
# LLM Model,
# Model de vectorisation
# Pipeline Input

#TODO: ajouter des les valeurs dans le ConfiVar Enum

def initLLM():
    return OllamaLLM(
        base_url="http://localhost:11434", model="lfm2.5-thinking:latest", temperature=0.35
    )


def initMilvus():

    URI = DB_URI

    client = MilvusClient(uri="http://localhost:19530", timeout=1000) # If not set, the timeout defaults to 10s
    return Milvus(
        embedding_function=EmbedModel(),
        connection_args={"uri": URI},
        index_params={"index_type": "FLAT", "metric_type": "COSINE"},
        drop_old=True,
        auto_id=True
    )


def EmbedModel():
    return OllamaEmbeddings(
        model="nomic-embed-text:latest",
        base_url="http://localhost:11434")

class PipelineInputs(TypedDict):
    request: str
    vectorStore: VectorStore
    llm: OllamaLLM
    embeder: Embeddings