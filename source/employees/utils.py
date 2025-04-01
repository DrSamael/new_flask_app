# from datetime import datetime
# from bson.objectid import ObjectId
#
# from source.daily_logs.crud import retrieve_daily_logs
# from source.employees.crud import retrieve_employee
# from source.projects.crud import retrieve_project
#
#
# def calculate_employee_wages(employee_id, month, year):
#     try:
#         employee_id = ObjectId(employee_id)
#     except:
#         return {"error": "Invalid employee ID"}, 400
#
#     start_date = datetime(year, month, 1)
#     end_date = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
#
#     statement = {"employee_id": employee_id, "created_at": {"$gte": start_date, "$lt": end_date}}
#     logs = retrieve_daily_logs(statement)
#
#     employee = retrieve_employee(employee_id)
#     if not employee:
#         return {"error": "Employee not found"}, 404
#
#     position_coefficient = employee.get("position", {}).get("coefficient", 1)
#     pay_rate = employee.get("qualification", {}).get("pay_rate", 1)
#
#     salary_by_project = {}
#     hours_by_project = {}
#     total_salary = 0
#     total_hours = 0
#
#     for log in logs:
#         execution_time = log["execution_time"]
#         project_id = log["project_id"]
#
#         project = retrieve_project(project_id)
#         if not project:
#             return {"error": f"Project with ID {project_id} not found"}, 404
#
#         project_name = project.get("title")
#         project_coefficient = project.get("category", {}).get("coefficient", 1) if project else 1
#
#         salary = execution_time * position_coefficient * pay_rate * project_coefficient
#         total_salary += salary
#         total_hours += execution_time
#
#         if project_name not in salary_by_project:
#             salary_by_project[project_name] = 0
#             hours_by_project[project_name] = 0
#
#         salary_by_project[project_name] += salary
#         hours_by_project[project_name] += execution_time
#
#     return {
#         "employee_id": str(employee_id),
#         "employee_name": employee["name"],
#         "month": month,
#         "year": year,
#         "salary_by_project": salary_by_project,
#         "hours_by_project": hours_by_project,
#         "total_hours": total_hours,
#         "total_salary": total_salary
#     }
