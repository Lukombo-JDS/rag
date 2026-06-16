from enum import Enum



def _overlap_algo(chunkSize: int = 4500) -> str:
    chunk_size: float = int(chunkSize)
    return int(chunk_size * 0.155)



DEFAULT_PATH:str = "./data/nba-rules.pdf"

DB_URI:str = "http://localhost:19530"

SPACY_SPLITTER_MAX_LENGTH = 10_000_000  # longueur maximum de caractères le model va prendre pour la création des chunks
# TODO: faire une script qui gère la valeur du max_length selon un type de métadonnée extrait et les performance d'extraction

SPLITTER_SEPARATOR = "\n\n"
 # TODO: créer un méthode qui gère les méthodes de manières plus intelligente.

SPLITTER_CHUNKS = 1024

SPLITTER_CHUNKS_OVERLAP = _overlap_algo(
    SPLITTER_CHUNKS
)  # valeur du nombre des caractères répétés entre 2 chunks successifs.

EMBED_DEFAULT_MODEL_NAME = "qwen3-embedding:0.6b"

EMBED_MODEL_NAME = "qwen3-embedding:0.6b"

EMBED_MODEL_BASE_URL = "http://localhost:11434"

LLM_MODEL_NAME = "lfm2.5-thinking:latest"

LLM_BASE_URL = "http://localhost:11434"

LLM_TEMPERATURE = 0.35

REQUEST_DEFAULT = "De quoi parle ce document ?"


class RetrievalPrompt:
    def __init__(self, request, context):
        self.request = request
        self.context = context

    def generate_prompt(self) -> str:
        return f"""
                You have to exactly answer the following question:\n\n
                {self.request}\n\n

                Based on the followin context:\n\n
                {self.context}\n\n
                You must give a short and precise answer that fits the question.

                Your answer:\n\n
                """

    # def get_retrieval_prompt(self)->str:
    #     return f"""
    #             You have to exactly answer the following question:

        
    #     """