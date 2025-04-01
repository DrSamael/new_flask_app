from source.employees.crud import retrieve_employees
from .wages_calculator import wages_calculator


def calculate_all_employees_wages(month, year):
    employees = retrieve_employees()
    if not employees:
        return {"error": "No employees found"}, 404

    results = []

    for employee in employees:
        res = wages_calculator(employee, month, year)
        results.append(res)

    return results
