from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, this is my first FastAPI app."}

@app.get("/hello-world/{user_id}")
async def hello(user_id:int):
    return {"message": f"Hello world. This is another test get response. User Id: {user_id}"}
