from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters.base import TokenTextSplitter
from transformers import AutoTokenizer

def Splitter(model: str)-> TokenTextSplitter:

    try:

        tokenizer = AutoTokenizer.from_pretrained(model)

        splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(tokenizer)

    except Exception as err:
        print("Splitter func ERROR: ", err)
        exit()
    
    return splitter


    