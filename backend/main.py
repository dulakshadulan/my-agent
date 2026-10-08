from fastapi import FastAPI

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