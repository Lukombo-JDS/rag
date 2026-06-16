from scripts.pipeline import PipelineInputs
from scripts.init import EmbedModel, initLLM, initMilvus
from scripts.pipeline import retrievePipeline
from scripts.var import * 
from scripts.transformation import injestion
from scripts.extraction import extractContents

def output(request:str):

    milvus_client = initMilvus()

    injestion(
        extractContents(),
        milvus_client
    )

    inputs: PipelineInputs = {
        "request": request,
        "embedder": EmbedModel(),
        "vectorStore": initMilvus(),
        "llm": initLLM(),
    }
    print("Hello from poc!")
    print("Vector DB ready !")

    for stream_chunks in retrievePipeline.stream(inputs):
        print(stream_chunks, end="", flush=True)
