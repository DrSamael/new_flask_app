from bson.objectid import ObjectId

from source.database import projects_collection
from source.projects.schemas import project_schema
from source.utils import serialize_doc
from source.projects.validations.validate_customer import validate_customer_eligibility


def add_project(data):
    errors = project_schema.validate(data)
    if errors:
        return {"error": errors}, 400

    validation_error = validate_customer_eligibility(data["customer_id"])
    if validation_error:
        return validation_error

    project = project_schema.load(data)
    project_id = projects_collection.insert_one(project).inserted_id

    new_project = projects_collection.find_one({"_id": project_id})
    return serialize_doc(new_project)


def retrieve_projects():
    projects = projects_collection.find()
    return [serialize_doc(project) for project in projects]


def retrieve_project(project_id):
    project = projects_collection.find_one({"_id": ObjectId(project_id)})
    if not project:
        return {"error": "Project not found"}, 404
    return serialize_doc(project)


def update_project(project_id, data):
    result = projects_collection.update_one({"_id": ObjectId(project_id)}, {"$set": data})
    if result.matched_count == 0:
        return {"error": "Project not found"}, 404

    updated_project = projects_collection.find_one({"_id": ObjectId(project_id)})
    return serialize_doc(updated_project)


def delete_project(project_id):
    result = projects_collection.delete_one({"_id": ObjectId(project_id)})
    if result.deleted_count == 0:
        return {"error": "Project not found"}, 404
    return {"message": "Project deleted"}
