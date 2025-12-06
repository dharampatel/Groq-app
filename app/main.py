import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(api_key=GROQ_API_KEY, model='llama-3.1-8b-instant')


@app.get('/hello')
def greetings():
    return {"message": "Hello, how are you?"}

@app.get('/generate')
def generate(query:str):
    response = llm.invoke(query)
    print(response)
    return {"msg": response.content}

if __name__ == "__main__":
    print(llm.invoke("Hello groq").content)