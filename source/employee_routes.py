from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId

from source.database import employees_collection

employee_bp = Blueprint("employee_bp", __name__)


@employee_bp.route("/", methods=["POST"])
def create_employee():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Missing required field: name"}), 400

    employee_id = employees_collection.insert_one({"name": data["name"]}).inserted_id
    return jsonify({"id": str(employee_id), "name": data["name"]}), 201


@employee_bp.route("/", methods=["GET"])
def get_employees():
    employees = employees_collection.find()
    return jsonify([{"id": str(emp["_id"]), "name": emp["name"]} for emp in employees])


@employee_bp.route("/<employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify({"id": str(employee["_id"]), "name": employee["name"]})


@employee_bp.route("/<employee_id>", methods=["PUT"])
def update_employee(employee_id):
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Missing required field: name"}), 400

    result = employees_collection.update_one({"_id": ObjectId(employee_id)}, {"$set": {"name": data["name"]}})
    if result.matched_count == 0:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify({"id": employee_id, "name": data["name"]})


@employee_bp.route("/<employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    result = employees_collection.delete_one({"_id": ObjectId(employee_id)})
    if result.deleted_count == 0:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify({"message": "Employee deleted"})
