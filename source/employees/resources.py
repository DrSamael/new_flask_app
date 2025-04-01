from flask_restful import Resource
from flask import request

from source.employees.crud import add_employee, retrieve_employees, retrieve_employee, update_employee, delete_employee
from source.employees.services.calculate_employee_wages import calculate_employee_wages
from source.employees.services.calculate_all_employees_wages import calculate_all_employees_wages


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


class EmployeeWageResource(Resource):
    def get(self, employee_id):
        month = request.args.get("month", type=int)
        year = request.args.get("year", type=int)

        if not month or not year:
            return {"error": "month and year parameters are required"}, 400

        return calculate_employee_wages(employee_id, month, year)


class EmployeeAllWageResource(Resource):
    def get(self):
        month = request.args.get("month", type=int)
        year = request.args.get("year", type=int)

        if not month or not year:
            return {"error": "month and year parameters are required"}, 400

        return calculate_all_employees_wages(month, year)
