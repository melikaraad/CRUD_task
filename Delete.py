from fastapi import FastAPI
from model import ToDo
from mgdb import collection

app = FastAPI()

@app.delete("/toDos/{id}")
def delete_todo(id: int):
    collection.delete_one({'id': id})
    return {'message': 'Todo deleted'}

if __name__ == "__Delete__":
    app.run(debug=True)
