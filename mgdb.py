from pymongo import MongoClient
from model import ToDo

client = MongoClient()
db = client['toDo', ToDo]
collection = db['toDos', ToDo]
