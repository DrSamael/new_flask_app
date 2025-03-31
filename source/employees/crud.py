from datetime import datetime

from bson.objectid import ObjectId

from source.database import employees_collection
from source.employees.schemas import employee_schema
from source.utils import serialize_doc


def add_employee(data):
    errors = employee_schema.validate(data)
    if errors:
        return {"error": errors}, 400

    employee = employee_schema.load(data)
    employee["created_at"] = datetime.now()
    employee_id = employees_collection.insert_one(employee).inserted_id

    new_employee = employees_collection.find_one({"_id": employee_id})
    return serialize_doc(new_employee)


def retrieve_employees():
    employees = employees_collection.find()
    return [serialize_doc(emp) for emp in employees]


def retrieve_employee(employee_id):
    employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
    if not employee:
        return {"error": "Employee not found"}, 404
    return serialize_doc(employee)


def update_employee(employee_id, data):
    result = employees_collection.update_one({"_id": ObjectId(employee_id)}, {"$set": data})
    if result.matched_count == 0:
        return {"error": "Employee not found"}, 404

    updated_employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
    return serialize_doc(updated_employee)


def delete_employee(employee_id):
    result = employees_collection.delete_one({"_id": ObjectId(employee_id)})
    if result.deleted_count == 0:
        return {"error": "Employee not found"}, 404
    return {"message": "Employee deleted"}
