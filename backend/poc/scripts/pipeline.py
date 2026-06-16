from scripts.init import PipelineInputs
from langchain_core.runnables import chain
from scripts.var import RetrievalPrompt
from langchain_core.vectorstores import VectorStore
from langchain_core.embeddings import Embeddings


@chain
def retrievePipeline(inputs: PipelineInputs):
    request: str = inputs["request"]
    vectorStore: VectorStore = inputs["vectorStore"]
    llm: OllamaLLM = inputs["llm"]
    embedder: Embeddings = inputs["embedder"]

    embeddedRequest = embedder.embed_query(request)

    results = vectorStore.similarity_search_by_vector(
        embedding=embeddedRequest,
    )
    retrieved = vectorStore.as_retriever(
        search_type = "mmr",
        search_kwargs = {
            "fetch_k": 5,
            "k": 3
        }
    )

    print("results: ", results[0])

    context = "\n\n".join(doc.page_content for doc in retrieved)

    print("CONTEXT REMONTÉE: ",context)

    prompt = RetrievalPrompt(request=request,context=context).generate_prompt()

    for chunk in llm.stream(prompt):
        yield chunk