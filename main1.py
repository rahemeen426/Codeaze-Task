from typing import Union
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def root():
    return {"name":"Rahemeen Khan", "message": "Hello World"}

@app.get("/items/{item_id}")
def index(item_id:int):
    return {"Product_id":item_id}