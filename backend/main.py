from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API = os.getenv("GEMINI_API_KEY")

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/health")
async def health():
    return {"status": "ok" ,"message" : "Server is running" }

@app.get("/users/{user_id}")
async def read_user(user_id  :str):
    return {"user" : user_id}

@app.get("/getapi")
async def display():
    return {"api" : GEMINI_API}

