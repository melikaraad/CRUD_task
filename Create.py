from fastapi import FastAPI
from model import ToDo
from mgdb import collection

app = FastAPI()

@app.post("/toDos")
def create_todo(toDo: ToDo):
    collection.insert_one(toDo.dict())
    return toDo
  
if __name__ == "__Create__":
    app.run(debug=True)

