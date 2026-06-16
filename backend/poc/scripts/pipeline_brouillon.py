from typing import TypedDict,Iterable
from langchain_core.documents.base import Document
from langchain_core.embeddings.embeddings import Embeddings
from langchain_core.language_models.llms import LLM
from langchain_core.runnables import chain
from langchain_core.vectorstores import VectorStore,VectorStoreRetriever
from langchain_milvus.vectorstores.milvus import MilvusClient,Milvus
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_pymupdf4llm.pymupdf4llm_loader import PyMuPDF4LLMLoader
from langchain_text_splitters.spacy import SpacyTextSplitter
# from pymilvus.milvus_client import MilvusClient
from var import *
from rich.traceback import install

install()


# Get Documnets

def extractContents(path:str):
    return PyMuPDF4LLMLoader(file_path=path).lazy_load()

# chunking logic 

def chunk_logic(page_token_size:int, nb_size:int, device_capacity):
    pass

# Chunking of documents content

def chunking(contents: Iterable[Document]) -> list[Document]:

    # print("pre-chunking-docs: ", contents[:1])

    splitter = SpacyTextSplitter(
        chunk_size=SPLITTER_CHUNKS,
        chunk_overlap=SPLITTER_CHUNKS_OVERLAP,
        max_length=SPACY_SPLITTER_MAX_LENGTH,
        separator=SPLITTER_SEPARATOR
        )

    return splitter.split_documents(contents)


def transformation(docs_path: str)->list[Document]:
    return chunking(
        extractContents(docs_path)
    )

# Init Vectore Store

def initMilvus(embedder: Embeddings) -> MilvusClient:
    # print("URI Milvus: ", DB_URI)

    # MC = MilvusClient(uri=DB_URI)
    try:

        M = Milvus(
            embedding_function=embedder,
            collection_name="nba_rules",
            connection_args={
                "uri": DB_URI,  # depuis ton host
                # "uri": "http://milvus-standalone:19530",  # depuis un autre container du compose
            },
            index_params={
                "index_type": "HNSW",
                "metric_type": "COSINE",
                "params": {
                    "M": 64,
                    "efConstruction": 100,
                },
            },
            search_params={
                "metric_type": "COSINE",
                "params": {"ef": 64},
            },
            consistency_level="Session",
            drop_old=True,
            auto_id=True,
        )
        return M
    except Exception as err:
        print(err)
        return None


def EmbedModel()->Embeddings:
    return OllamaEmbeddings(model=EMBED_DEFAULT_MODEL_NAME, base_url=EMBED_MODEL_BASE_URL)


# Adding embed chunks to vector store

def embeddingContents(docs: list[Document], vectorStore: VectorStore, embeder: Embeddings)->VectorStore:

    try:
        e=embeder
        return vectorStore.from_documents(documents=docs,embedding=e)

    except Exception as err:
        print(err)
        return None



def embeddingRequest(request: str, embeder: Embeddings) -> list[float]:
    return embeder.embed_query(request)


def initLLM():
    return OllamaLLM(
        base_url=LLM_BASE_URL,
        model=LLM_MODEL_NAME,
        temperature=LLM_TEMPERATURE
    )


# Pipeline of the workflow of the RAG

class PipelineInputs(TypedDict):
    request: str
    vectorStore: VectorStore
    llm: OllamaLLM
    embeder: Embeddings


@chain
def retrievePipeline(inputs: PipelineInputs):
    request: str = inputs["request"]
    vectorStore: VectorStore = inputs["vectorStore"]
    llm: OllamaLLM = inputs["llm"]
    embedding_model: Embeddings = inputs["embeder"]


    # Inject docs into Vectore store
    vectorStore = embeddingContents(
        transformation(DEFAULT_PATH),
        vectorStore, 
        embedding_model
        )

    retriever = vectorStore.as_retriever(
        search_type="mmr",
        search_kwargs = {"k": 5,"lambda_mult":0.25}
        )

    results = retriever.invoke(input=request)

    print("DOCS FOUND: ", results[0])

    context = "\n\n".join(doc.page_content for doc in results)
    # score = "\n\n".join(doc.score for doc in results)

    print("CONTEXT DOCS: ",context)

    prompt_system = RetrievalPrompt(request,context).generate_prompt()

    for chunk in llm.stream(prompt_system):
        # print("!!!! chunks found:  ", chunk)
        yield chunk


def output(request: str, embedding_model: Embeddings):
    db_vectoriel = initMilvus(embedding_model)

    inputs: PipelineInputs = {
        "request": request,
        "embeder": embedding_model,
        "vectorStore": db_vectoriel,
        "llm": initLLM(),
    }
    print("Hello from poc!")
    print("Vector DB ready!")

    for chks in retrievePipeline.stream(inputs):

        print(chks, end="", flush=True)


embed_model = EmbedModel()

output("Cite me 3 faults in this document", embed_model)