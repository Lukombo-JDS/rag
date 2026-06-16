# Mon Journal

## Quoi

Construire un RAG: founire des documents et poser des questions sur le(s) documents injectés.

## Pourquoi

Pour montrer mon avancé durant la programmation de ce RAG et rapporté mes difficultés.

## Comment

Je vais utiliser les langages, outils et framework suivant de cette stack:

AI : 
	- LLM : lfm2.5-thinking:latest (en local avec OLLAMA)
	- Embedding model : qwen3-embedding:0.6b (en local avec OLLAMA)


Backend : 
	- REST API : Golang (Chi)
	- AI service : FastAPI
	- SQL DB : LibSQL
		- ORM : Bun
	- Vector DB : Milvus Standalone (dans docker compose)
	- AI Framework : Langchain
	- Swagger

Frontend : 
	- nuxt4
	- shadcn/nuxt
	- Tailwind/CSS
	- TS
	- gradio (pour le poc)

Versioning: 

	- jujutsu au-dessus de git

## Résultats

Un frontend qui permet de charger les fichiers et de poser des questions sur les fichiers.
Une API backend RAG qui permet de d'être suffisamment générique pour le réutiliser dans d'autres projets.


## Log

### 15 - Juin - 2026 | le début de l'aventure

Je vais refactor un projet que j'avais commencer pour construire ce RAG portfolio.

### 18 - Juin - 2026 | Correction sur des erreurs & finalisation du poc monofichier

Le PoC est en place mais il y'a des erreurs entre Milvus et Langchain.

Ajout de Taskfile pour créer des commandes courtes et des tâches récurrentes

j'ai eu un soucis avec la version : issue sur les verison de "langchain_milvus >= 2.9.0" --> la class Milvus n'arrive pas à se connecter via URI à milvus qui tourne dans le docker-compose en local dans ma machine.
Résolution : fixer la version à 2.9.0 car le problème survient dès >= 2.9.0.






