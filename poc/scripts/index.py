from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    get_response_synthesizer,
)
from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import (
    VectorContextRetriever,
    VectorIndexAutoRetriever,
    VectorIndexRetriever,
)
from llama_index.core.vector_stores.types import VectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores import milvus
from llama_index.vector_stores.milvus.base import MilvusVectorStore

# Get documents


def getDocs():

    return SimpleDirectoryReader("./data").load_data(show_progress=True)


def vectorStoreIndex(vectorStore, embeddingType):

    return VectorStoreIndex.from_vector_store(
        embed_model=embeddingType, vector_store=vectorStore
    )


def vectorIndexRetriever(
    vectorIndex: VectorStoreIndex, embedModel: BaseEmbedding, vectorStore: VectorStore
):
    return


# model Embedding


def embedModel():

    return OllamaEmbedding(
        model_name="nomic-embed-text:latest",
    )


def initMilvus():

    # Vector store
    milvus_db = milvus.MilvusVectorStore(
        collection_name="rag-poc",
        similarity_metric="COSINE",
        dim=768,
        embedding_field="vectors",
        grpc_options={
            "grpc.keepalive_time_ms": 20 * 1000,  # 5 min
            "grpc.keepalive_timeout_ms": 10000,
            "grpc.keepalive_permit_without_calls": False,
        },
    )
    return milvus_db


# Pipeline


def pipeline(
    docs,
    vector_index: VectorStoreIndex,
    vectorStore: MilvusVectorStore,
    collection_name,
    embedModel: BaseEmbedding,
):

    ollama_llm = Ollama
    ollama_llm.model = "ministral-3:3b"
    ollama_llm.temperature = 0.3

    ollama_llm.system_prompt = """
				Tu dois répondre en faisant une synthèse des relevés selon le contexte."""

    vectRetriever = VectorIndexRetriever(
        index=vector_index,
        embed_model=embedModel,
        vectore_store=vectorStore,
        similarity_top_k=3,
        verbose=True,
    )

    pipeline = IngestionPipeline(
        name="rag-poc",
        transformations=[
            SentenceSplitter(
                chunk_size=550,
                chunk_overlap=5,
                paragraph_separator="\n\n",
                include_metadata=False,
            ),
            embedModel,
        ],
        documents=docs,
        vector_store=vectorStore,
    )

    pipeline.run()

    vectRetriever

    vectorStore.client.load_collection(collection_name)

    return query_engine.retrieve


# outputs


def retrieveResults(nodes: NodeW):
	nodes 
    print(f" *** Nodes ---> {nodes} *** ")
    for i, node in enumerate(nodes):
        print(f"--- Résultat n°{i + 1} (Score de similarité : {node.score:.4f}) ---")
        print("TEXT: ", node.text)
        print(node)
        print("\n")
