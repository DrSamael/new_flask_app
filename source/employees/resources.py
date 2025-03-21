from flask_restful import Resource
from flask import request

from source.employees.crud import add_employee, retrieve_employees, retrieve_employee, update_employee, delete_employee


class EmployeeListResource(Resource):
    def get(self):
        return retrieve_employees()

    def post(self):
        data = request.json
        return add_employee(data)


class EmployeeResource(Resource):
    def get(self, employee_id):
        return retrieve_employee(employee_id)

    def put(self, employee_id):
        data = request.json
        return update_employee(employee_id, data)

    def delete(self, employee_id):
        return delete_employee(employee_id)
