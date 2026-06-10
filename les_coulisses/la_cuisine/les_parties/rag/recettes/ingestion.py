import filetype
from typing import LiteralString,Literal,TextIO
from langchain_core.documents.base import Document
from langchain_pymupdf4llm.pymupdf4llm_loader import PyMuPDF4LLMLoader
import os
from enum import Enum

class Extension(Enum):
    PDF = "pdf"
    TXT = "txt"

MODE = "page"

def checkDoc(path: str)->bool|None:
    file_ext:str = filetype.guess_extension(path)
    if file_ext == (Extension.PDF or Extension.TXT) :
        return None
    else:
        with open(path, mode="r") as f:
            if not f.readable():
                return False
            else:
                return True


#~~TODO: les transformer en type Document de langchain~~
    #~~TODO: récupérer le contenu de la page et les metadata~~
    #TODO: ~~les rentrer dans le type Document si besoin~~

def transfomPDF(path: str)->list[Document]:

    return PyMuPDF4LLMLoader(path,mode=MODE).load()

def tranformText(path:str):

    content:list[Document]
  

  
    with open(path, "r") as f:
        content=f.readlines()
    

    


    return 
