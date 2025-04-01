from datetime import datetime
from bson.objectid import ObjectId

from source.database import project_budgets_collection
from source.project_budgets.schemas import project_budget_schema
from source.utils import serialize_doc


def add_project_budget(data):
    errors = project_budget_schema.validate(data)
    if errors:
        return {"error": errors}, 400

    project_budget = project_budget_schema.load(data)
    project_budget["created_at"] = datetime.now()
    project_budget_id = project_budgets_collection.insert_one(project_budget).inserted_id

    new_project_budget = project_budgets_collection.find_one({"_id": project_budget_id})
    return serialize_doc(new_project_budget)


def retrieve_project_budgets():
    project_budgets = project_budgets_collection.find()
    return [serialize_doc(customer) for customer in project_budgets]


def retrieve_project_budget(project_budget_id):
    project_budget = project_budgets_collection.find_one({"_id": ObjectId(project_budget_id)})
    if not project_budget:
        return {"error": "Project budget not found"}, 404
    return serialize_doc(project_budget)


def update_project_budget(project_budget_id, data):
    result = project_budgets_collection.update_one({"_id": ObjectId(project_budget_id)}, {"$set": data})
    if result.matched_count == 0:
        return {"error": "Project budget not found"}, 404

    updated_project_budget = project_budgets_collection.find_one({"_id": ObjectId(project_budget_id)})
    return serialize_doc(updated_project_budget)


def delete_project_budget(project_budget_id):
    result = project_budgets_collection.delete_one({"_id": ObjectId(project_budget_id)})
    if result.deleted_count == 0:
        return {"error": "Project budget not found"}, 404
    return {"message": "Project budget deleted"}
