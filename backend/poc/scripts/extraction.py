from langchain_pymupdf4llm.pymupdf4llm_loader import PyMuPDF4LLMLoader
from scripts.var import *
from scripts.vectorisation import *
from scripts.init import initMilvus


# Récupérer le contenu du document

def extractContents(path:str):
    return PyMuPDF4LLMLoader(file_path=path).lazy_load()