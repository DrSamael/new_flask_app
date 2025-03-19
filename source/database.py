from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["new_flask_app_db"]
employees_collection = db["employees"]
