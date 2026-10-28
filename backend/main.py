from fastapi import FastAPI
import os
from dotenv import load_dotenv
from google import genai
from models.gemini_provider import GeminiProvider

provider = GeminiProvider()

load_dotenv()

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

@app.get("/api/{input_txt}")
async def api_call(input_txt : str):
    res = await provider.model_call(input_txt)
    return res