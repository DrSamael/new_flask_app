from flask import Blueprint

from source.employees.resources import EmployeeListResource, EmployeeResource

employee_bp = Blueprint("employee_bp", __name__)


def initialize_routes(api):
    api.add_resource(EmployeeListResource, "/employees")
    api.add_resource(EmployeeResource, "/employees/<string:employee_id>")
