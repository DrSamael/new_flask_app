from flask import Flask
from flask_restful import Api

from source.employees.routes import initialize_routes as initialize_employee_routes
from source.projects.routes import initialize_routes as initialize_project_routes
from source.customers.routes import initialize_routes as initialize_customer_routes
from source.daily_logs.routes import initialize_routes as initialize_daily_log_routes
from source.project_budgets.routes import initialize_routes as initialize_project_budgets_routes

app = Flask(__name__)
api = Api(app)

initialize_employee_routes(api)
initialize_project_routes(api)
initialize_customer_routes(api)
initialize_daily_log_routes(api)
initialize_project_budgets_routes(api)

if __name__ == "__main__":
    app.run(debug=True)
