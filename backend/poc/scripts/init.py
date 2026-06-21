from langchain_core.embeddings.embeddings import Embeddings
from langchain_ollama.llms import OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_milvus import Milvus
from typing import TypedDict
from langchain_core.vectorstores import VectorStore
from .var import (
    LLM_BASE_URL,
    LLM_MODEL_NAME,
    LLM_TEMPERATURE,
    DB_URI,
    COLLECTION_NAME_DEFAULT,
    EMBED_MODEL_NAME,
    EMBED_MODEL_DIM,
    EMBED_MODEL_BASE_URL
)

# Initialisation:
# BDD Vectorielle,
# LLM Model,
# Model de vectorisation
# Pipeline Input

def initLLM():
    return OllamaLLM(
        base_url=LLM_BASE_URL,
        model=LLM_MODEL_NAME,
        temperature=LLM_TEMPERATURE
    )


# Init Vectore Store

def initMilvus(embedder: Embeddings, collection_name:str = COLLECTION_NAME_DEFAULT) -> Milvus:


    # MC = MilvusClient(uri=DB_URI)
    try:

        M = Milvus(
            embedding_function=embedder,
            collection_name=collection_name,
            connection_args={
                "uri": DB_URI,  # depuis ton host
                # "uri": "http://milvus-standalone:19530",  # depuis un autre container du compose
            },
            index_params = {
                "index_type": "HNSW",
                "metric_type": "COSINE",
                "params": {
                    "M": 64,
                    "efConstruction": 100,
                },
            },
            search_params = {
                "metric_type": "COSINE",
                "params": {"ef": 64},
            },
            consistency_level="Session",
            drop_old=True,
            auto_id=True,
        )
        
    except Exception as err:
        print("Exception init Milvus: ", err)
        exit()
    return M

def EmbedModel():
    model = OllamaEmbeddings(
        model=EMBED_MODEL_NAME,
        base_url=EMBED_MODEL_BASE_URL
        )
    model.dimensions = EMBED_MODEL_DIM
    return model

class PipelineInputs(TypedDict):
    request: str
    vectorStore: VectorStore
    llm: OllamaLLM
    embeder: Embeddings