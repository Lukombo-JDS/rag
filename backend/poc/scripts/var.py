import ollama


 # TODO: créer un méthode qui gère les méthodes de manières plus intelligente.

def _overlap_algo(chunkSize: int = 4500) -> int:
    chunk_size: float = int(chunkSize)
    return int(chunk_size * 0.155)

def _get_model_dim(model_name:str) -> int:
    
    res = ollama.embed(model=model_name,input="Un test pour avoir la dimensionn des vecteurs du model")

    vec = res["embeddings"][0]
    
    return len(vec)
    

DEFAULT_PATH:str = "./data/nba-rules.pdf"

DB_URI:str = "http://localhost:19530"
DB_MILVUS_URI = "../milvus.db"

SPACY_SPLITTER_MAX_LENGTH = 10_000_000  # longueur maximum de caractères le model va prendre pour la création des chunks
# TODO: faire une script qui gère la valeur du max_length selon un type de métadonnée extrait et les performance d'extraction

SPLITTER_SEPARATOR = ["\n\n", "\t", "\t\t"]

SPLITTER_CHUNKS = 500

SPLITTER_CHUNKS_OVERLAP = _overlap_algo(
    SPLITTER_CHUNKS
)  # valeur du nombre des caractères répétés entre 2 chunks successifs.

EMBED_DEFAULT_MODEL_NAME = "embeddinggemma:300m"

EMBED_DEFAULT_MODEL_HF = "google/embeddinggemma-300m-qat-q8_0-unquantized"

EMBED_MODEL_NAME = "embeddinggemma:300m"

EMBED_MODEL_BASE_URL = "http://localhost:11434"

EMBED_MODEL_DIM = _get_model_dim(EMBED_MODEL_NAME)

LLM_MODEL_NAME = "lfm2.5-thinking:latest"

# LLM_MODEL_NAME = "qwen3.5:0.8b"

LLM_BASE_URL = "http://localhost:11434"

LLM_TEMPERATURE = 0.1

INDEX_TYPE = "HNSW"

METRIC_TYPE = "IP"

DEFAULT_REQUEST = "De quoi parle ce document ?"

MMR_K = 5

MMR_LAMBDA = 0.25

MMR_SEARCH_KWARGS = {
    "k": MMR_K,
    "lambda_mult": MMR_LAMBDA
    }

SEARCH_TYPE_RETRIEVER = "mmr"

COLLECTION_NAME_DEFAULT = "rag_user_default"


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
                You must give a response that fit the question the most.

                Your answer:\n\n
                """