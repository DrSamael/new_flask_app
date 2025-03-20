from flask import Blueprint, request, jsonify

from source.employees.schemas import employee_schema
from source.employees.crud import add_employee, retrieve_employees, retrieve_employee, update_employee, delete_employee

employee_bp = Blueprint("employee_bp", __name__)


@employee_bp.route("/", methods=["POST"])
def create_employee():
    data = request.json
    errors = employee_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    return add_employee(data), 200


@employee_bp.route("/", methods=["GET"])
def get_employees():
    return retrieve_employees(), 200


@employee_bp.route("/<employee_id>", methods=["GET"])
def get_employee(employee_id):
    return retrieve_employee(employee_id), 200


@employee_bp.route("/<employee_id>", methods=["PUT"])
def edit_employee(employee_id):
    data = request.json
    errors = employee_schema.validate(data, partial=True)
    if errors:
        return jsonify({"error": errors}), 400

    return update_employee(employee_id, data)


@employee_bp.route("/<employee_id>", methods=["DELETE"])
def destroy_employee(employee_id):
    return delete_employee(employee_id), 204
