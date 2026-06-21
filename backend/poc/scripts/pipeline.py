from .init import PipelineInputs
from langchain_core.runnables import chain
from scripts.var import RetrievalPrompt
from langchain_core.vectorstores import VectorStore
from langchain_core.embeddings import Embeddings
from .vectorisation import embeddingContents
from .transformation import transformation
from .var import DEFAULT_PATH
from .init import OllamaLLM

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
        search_kwargs={"k": 50})

    results = retriever.invoke(input=request) 

    context = "\n\n".join(doc.page_content for doc in results)

    prompt_system = RetrievalPrompt(request,context).generate_prompt()

    for chunk in llm.stream(prompt_system):
        yield chunk