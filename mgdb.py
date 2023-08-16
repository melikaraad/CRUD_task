from pymongo import MongoClient
from model import ToDo

client = MongoClient()
db = client['toDo']
collection = db['toDos']
