from llama_index.core import Settings, VectorStoreIndex
from llama_index.core.readers import SimpleDirectoryReader
from llama_index.core.storage.storage_context import StorageContext
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.milvus import MilvusVectorStore

# --- ÉTAPE A : Configurer Ollama (LLM et Embeddings) ---
# Configuration du modèle pour répondre aux questions
llm_local = Ollama(model="qwen2.5:3b", request_timeout=120.0)

# Configuration du modèle pour vectoriser tes documents 
# (Ollama sait utiliser le même modèle ou un modèle dédié aux embeddings)
embed_local = OllamaEmbedding(model_name="nomic-embed-text:latest")

# --- ÉTAPE B : Définir les réglages globaux (Settings) ---
# On dit à LlamaIndex d'utiliser Ollama par défaut pour tout le projet
settings = Settings
settings.llm = llm_local
settings.embed_model = embed_local

# --- ÉTAPE C : Configurer le Stockage Milvus ---
vector_store = MilvusVectorStore(
    collection_name="rag_local_ollama",
    dim=768,  # /!\ Attention: La dimension dépend du modèle (ex : Llama 3 = 4096, Mistral = 4096)
)

storage_context = StorageContext.from_defaults(vector_store=vector_store)

# --- ÉTAPE D : Ingestion et Requête ---
documents = SimpleDirectoryReader("data/").load_data()


# L'index va automatiquement utiliser l'embed_model (Ollama) défini dans les Settings
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, show_progress=True
)

# Créer le moteur de recherche et poser la question
query_engine = index.as_query_engine()
reponse = query_engine.query("Quelles sont les instructions importantes à retenir ?")