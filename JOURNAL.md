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


## Log: 

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


