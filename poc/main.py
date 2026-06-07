from scripts.index import (
    embedModel,
    getDocs,
    initMilvus,
    pipeline,
    retrieveResults,
    vectorStoreIndex,
)


def main():
    print("Hello from poc!")

    milvus_lite = initMilvus()

    print("Vector DB ready !")

    nodes = pipeline(
        docs=getDocs(),
        vector_index=vectorStoreIndex(milvus_lite, embedModel()),
        vectorStore=milvus_lite,
        collection_name="rag-poc",
    )

    print("Pipeline Ready !")

    print("Retrieve: ")

    retrieveResults(nodes)


if __name__ == "__main__":
    main()
