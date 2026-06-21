from vectorisation import check_vec_norm
from collections.abc import Iterable,Iterator
from typing import TypedDict

from langchain_core.documents.base import Document
from langchain_core.embeddings.embeddings import Embeddings
from langchain_core.runnables import chain
from langchain_core.vectorstores.base import VectorStore
from langchain_milvus.vectorstores.milvus import Milvus
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_pymupdf_layout.pymupdf_layout_loader import PyMuPDFLayoutLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rich.traceback import install
from vectorisation import normalization
from var import (
    EMBED_MODEL_NAME,
    DB_MILVUS_URI,
    DEFAULT_PATH,
    EMBED_DEFAULT_MODEL_NAME,
    EMBED_MODEL_BASE_URL,
    EMBED_MODEL_DIM,
    LLM_BASE_URL,
    LLM_MODEL_NAME,
    LLM_TEMPERATURE,
    SPLITTER_SEPARATOR,
    RetrievalPrompt,
)

install()


# Get Documnets


def extractContents(path: str):
    # PyMuPDFLayoutLoader(file_path=path).lazy_load()
    return PyMuPDFLayoutLoader(file_path=path).lazy_load()


# Chunking of documents content


def chunking(contents: Iterable[Document]) -> list[Document]:

    try:
        # tokenizer = AutoTokenizer.from_pretrained(EMBED_DEFAULT_MODEL_HF)

        splitter = RecursiveCharacterTextSplitter(separators=SPLITTER_SEPARATOR)

        # splitter.transform_documents(contents)

    except Exception as err:
        print("Chunking function ERROR: ", err)
        exit()

    return splitter.split_documents(contents)


def transformation(docs_path: str) -> list[Document]:
    return chunking(extractContents(docs_path))


# Init Vectore Store

def initMilvus() -> Milvus: 

    try:
        M = Milvus(
            embedding_function=EmbedModel(),
            collection_name="nba",
            connection_args={
                "uri": DB_MILVUS_URI,  # depuis ton host
                # "uri": "http://milvus-standalone:19530",  # depuis un autre container du compose
            },
            index_params={
                "index_type": "HNSW ",
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
            drop_old=False,
            auto_id=True,
        )

    except Exception as err:
        print(err)
        exit()

    return M

def EmbedModel() -> Embeddings:
    model = OllamaEmbeddings(
        model=EMBED_DEFAULT_MODEL_NAME, base_url=EMBED_MODEL_BASE_URL, dimensions=EMBED_MODEL_DIM
    )

    return model


# Adding embeding chunks into vector store


def embeddingContents(
    docs: list[Document], vectorStore: VectorStore, embeder: Embeddings
) -> VectorStore:

    if not check_vec_norm(EMBED_MODEL_NAME):

       try:
            e = embeder
            # e.embed_documents()
            vectorStore.add_documents(documents=docs, embedding=e)
    
            if vectorStore.embeddings:
    
                vectors = vectorStore.embeddings.embed_documents(
                    texts=[d.page_content for d in docs]
                    )
    
                normed_vectors = normalization(vectors)
    
                initMilvus().add_embeddings(
                    texts = [d.page_content for d in docs],
                    embeddings = normed_vectors)
    
    
       except Exception as err:
            print(err)
            exit()

    return vectorStore


def embeddingRequest(request: str, embeder: Embeddings) -> list[float]:
    return embeder.embed_query(request)


def initLLM():
    return OllamaLLM(base_url=LLM_BASE_URL, model=LLM_MODEL_NAME, temperature=LLM_TEMPERATURE)


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
    vectorStore = embeddingContents(transformation(DEFAULT_PATH), vectorStore, embedding_model)

    retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k": 50})

    results = retriever.invoke(input=request)

    context = "\n\n".join(doc.page_content for doc in results)

    prompt_system = RetrievalPrompt(request, context).generate_prompt()

    for chunk in llm.stream(prompt_system):
        yield chunk


#TODO: créer une chaine séquentielle
def run(request: str, embedding_model: Embeddings):

    db_vectoriel = initMilvus()

    llm = initLLM()

    inputs: PipelineInputs = {
        "request": request,
        "embeder": embedding_model,
        "vectorStore": db_vectoriel,
        "llm": llm,
    }
    print("Hello from poc!")
    print("Vector DB ready!")

    return retrievePipeline.stream(inputs)

def output(Pipeline: Iterator[str]):
    for chks in Pipeline:
        print(chks, end="", flush=True)


embed_model = EmbedModel()

output(
    run("the subject of the document", embed_model)
)
