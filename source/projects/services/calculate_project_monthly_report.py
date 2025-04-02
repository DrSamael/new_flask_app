from datetime import datetime
from bson import ObjectId, errors

from source.daily_logs.crud import retrieve_daily_logs
from source.projects.crud import retrieve_project
from source.employees.crud import retrieve_employee


def calculate_project_monthly_report(project_id, month, year):
    try:
        project_id = ObjectId(project_id)
    except errors.InvalidId:
        return {"error": "Invalid project ID"}, 400

    start_date = datetime(year, month, 1)
    end_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)

    statement = {"project_id": project_id, "created_at": {"$gte": start_date, "$lt": end_date}}
    logs = retrieve_daily_logs(statement)

    if not logs:
        return {"error": "No work logs found for this project in the given month"}, 404

    project = retrieve_project(project_id)
    if not project:
        return {"error": "Project not found"}, 404

    project_coefficient = project.get("category", {}).get("coefficient", 1)

    employee_data = {}
    total_hours = 0
    total_salary = 0

    for log in logs:
        execution_time = log["execution_time"]
        employee_id = log["employee_id"]

        if employee_id not in employee_data:
            employee = retrieve_employee(employee_id)
            if not employee:
                continue

            employee_data[employee_id] = {
                "employee_id": str(employee_id),
                "employee_name": employee["name"],
                "total_hours": 0,
                "total_salary": 0,
                "position_coefficient": employee.get("position", {}).get("coefficient", 1),
                "pay_rate": employee.get("qualification", {}).get("pay_rate", 1)
            }

        position_coefficient = employee_data[employee_id]["position_coefficient"]
        pay_rate = employee_data[employee_id]["pay_rate"]
        salary = execution_time * position_coefficient * pay_rate * project_coefficient

        employee_data[employee_id]["total_hours"] += execution_time
        employee_data[employee_id]["total_salary"] += salary
        total_hours += execution_time
        total_salary += salary

    return {
        "project_id": str(project_id),
        "project_title": project["title"],
        "project_category_coefficient": project.get("category", {}).get("coefficient", 1),
        "month": month,
        "year": year,
        "total_hours": total_hours,
        "total_salary": total_salary,
        "employees": list(employee_data.values())
    }
