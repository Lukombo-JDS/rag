from scripts.pipeline import PipelineInputs
from scripts.init import EmbedModel, initLLM, initMilvus
from scripts.pipeline import retrievePipeline

def output(request: str):

    embedder = EmbedModel()
    db_vectoriel = initMilvus(embedder)
    
    inputs: PipelineInputs = {
            "request": request,
            "embeder": embedder,
            "vectorStore": db_vectoriel,
            "llm": initLLM(),
        }
    for chks in retrievePipeline.stream(inputs):

        print(chks, end="", flush=True)
