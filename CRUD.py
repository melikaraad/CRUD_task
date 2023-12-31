from fastapi import FastAPI
from model import ToDo
from mgdb import collection

app = FastAPI()

@app.get("/toDos")
def get_todos():
    return collection.find()

@app.post("/toDos")
def create_todo(toDo: ToDo):
    collection.insert_one(toDo.dict())
    return toDo

@app.put("/toDos/{id}")
def update_todo(id: int, toDo: ToDo):
    collection.update_one({'id': id}, {'$set': toDo.dict()})
    return toDo
 
@app.delete("/toDos/{id}")
def delete_todo(id: int):
    collection.delete_one({'id': id})
    return {'message': 'Todo deleted'}


