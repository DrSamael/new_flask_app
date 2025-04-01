from source.employees.crud import retrieve_employee
from .wages_calculator import wages_calculator


def calculate_employee_wages(employee_id, month, year):
    employee = retrieve_employee(employee_id)
    if not employee:
        return {"error": "Employee not found"}, 404

    return wages_calculator(employee, month, year)
