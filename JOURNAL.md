# My Journey

## What

Building a API REST for RAG.

## Why

This is my journey to create a standard RAG without anny generative AI in order to have a solid exemple of a RAG in 2026.

## How 

Using open-source stack for the database, vector database and packages, dependencies to be free as possible.


## Draft Stack

Backend : 
	- REST API : Golang (Chi)
	- AI service : FastAPI
	- SQL DB : LibSQL
		- ORM : Bun
	- Vector DB : Milvus Standard
	- AI Framework : Langchain
	- Swagger

Frontend : 
	- nuxt4
	- shadcn/nuxt
	- Tailwind/CSS
	- TS

Versioning: 

	- jujutsu over git


## Log

### 26-05-2026 - All you Need is a restaurant

I found a way to better understand clean architecture ! I was struggling a lot about understand the concept and do it properly. It was very hard for me to do it the right way, the words for the folder and also learning POO concept and adding to all of that focusing on practicing Golang in SOLID concept too... 

When I ask GEMINI to give me a x time (Yeah I ask so many times to Chatbot the explanation), how I can code properly better in clean architecture concept. One thing in GEMINI response: one of the main concept of  Clean Architecture is to separate the code in multiple different level at least 3 I recall. End there a little spark in a light bulbe came to my mind... I ask "It's like in a Kitchen of a restaurant, right ?" and it respond "Yes you can view it as an architecture like a restaurant". After that everything because much more clear: 

I will applied it for the Modular Monolith architecture (IMO the only one that matter...)

The Restaurant = Your project 

The Backstage = Backend folder

The Dining Area = Frontend Folder

The Backstage (Backend Folder) =
	- Control Panel = Cmd/
	- The Kitchen = Internal/ (or core/)
		- Stations = Domain/ Entities/
	- The Pass = api/
	- Store Room = Infra/
		- Cold Storage = persistence/
		- pantry = cache/
	- Control room = devops/
	- Practice service = tests/

And you can apply the same logic to your "Frontend/" here aka Dining Area(I think we might inlcude the facade of the restaurant but you understand the logic here).

You may see some names of the folders, files, functions and variables in french, it's juste for me to understand before refactor in the more standard terms in english. -- And also some commits but through the project I will write in english.


### 28-08-2026 - Not the Good start

I'm back ! After some dicussion with a friend, he gave the advice that I should first do a simple functional code of a rag and then implemented everything step by step in monolith modular architecture more clean.
So today I will create a folder for to create the PoC...

### 2-06-2026 - I'm BACK !!

After few days doing other stuff (helping others alumnis for their projects), I'm going to continue the poc. 
I'm a little bit struggle to understand LlamaIndex: how to setup it is a little bit tidious, Langchain is more simple but a friend told me LlamaIndex is more fast and is more useful to be use in order to config RAG tools.
I'm just need to read a lot. BTW the docs is very all over the place to understant how to set up the framework...


### 5-06-2026 - Perseverance is a virtue

After a lot of reads and some rookie mistaks I'm finally able to : 

	- load a pdf file from a folder './poc/data/'
	- run the embedding for that file : working
	- Got the 
	- and get a response from the llm after asking a simple question ! (no just kidding my ): I got a problem with LlamaIndex --> I didn't set the Dimension of the vector for the embedding model

### 7-06-2026 - Bad Setups give you hiccups

After setting the vectore store and embedding model the right the pipeline is working !! 
I got the nodes scores but not the chunks retrieved. 
I need to understand more how nodes works in LlamaIndex...

### 


