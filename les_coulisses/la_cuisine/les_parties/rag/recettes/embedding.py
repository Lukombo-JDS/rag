from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents.base import Document
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores.base import VectorStore as VectDB

def chunking_files(docs: Document)->list(Document)|None:
    # use langachain for chunking documents.
    # return map(or hash map) : key == metadata vector / value == arrays of vectors

    doc_chunks:list(Document) = RecursiveCharacterTextSplitter(
        separators=["\n\n","\t", "\t\t"],
        keep_separator=True,
        chunk_size=500,
        overlap=50
    ).split_documents(documents=docs)
    


    return doc_chunks


def create_vectors(
    chunks: list[Document], 
    vector_store: VectDB
    )->list[str]|None:
    

    ids:list[str] = None

    for chk in chunks:
        
        ids.append(vector_store.add_documents(chk))


    return ids
        






