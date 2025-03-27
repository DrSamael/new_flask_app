from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["new_flask_app_db"]

employees_collection = db["employees"]
projects_collection = db["projects"]
customers_collection = db["customers"]
daily_logs_collection = db["daily_logs"]
project_budgets_collection = db["project_budgets"]
