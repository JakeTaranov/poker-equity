from pymongo.mongo_client import MongoClient
import certifi

client = MongoClient("mongodb+srv://taranovjake99:qhLl1FyUHzr9gpJr@poker-equity.4dx6cky.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())

db=client.todo_db

collection_name = db["todo_collection"]

