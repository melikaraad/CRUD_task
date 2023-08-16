from fastapi import FastAPI
from model import ToDo
from mgdb import collection

app = FastAPI()

@app.get("/toDos")
def get_todos():
    return collection.find()

if __name__ == "__Read__":
    app.run(debug=True)
