
from enum import Enum

class Provider(str, Enum):
    OLLAMA = "ollama"
    LMSTUDIO = "lmstudio"

class LLMModel:
        
