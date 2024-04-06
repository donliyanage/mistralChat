# MistralChat

Simple Mistral+Langchain+RAG based chat framework to build a chat assiatant.

Add RAG context PDFs in to the /data/ folder

Endpoint exported as a Flask service 

## exec

Run flask on handlerchat.py
endpoint will be on https://127.0.0.1/chat, as a POST HTTP endpoint. This will accept the chat as a data element with the format {'query':'XXXXX'}
