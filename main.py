from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool] = True



@app.get("/blog")
def home(limit : Optional[int]=None,published:bool=True):
    return {f"limit":limit,"published":published}

@app.get("/blog/{id}")
def show(id: int):
    return {"id": id}

@app.post("/blog")
def create(request: Blog):
    return {"data": request}