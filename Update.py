from fastapi import FastAPI
from model import ToDo
from mgdb import collection

app = FastAPI()

@app.put("/toDos/{id}")
def update_todo(id: int, toDo: ToDo):
    collection.update_one({'id': id}, {'$set': toDo.dict()})
    return toDo

if __name__ == "__Update__":
    app.run(debug=True)
