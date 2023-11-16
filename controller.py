from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    user_prompt: str

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.post("/query/")
async def create_item(item: Request):
    return 