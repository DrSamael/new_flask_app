from flask_restful import Resource
from flask import request

from source.project_budgets.crud import (add_project_budget, retrieve_project_budgets, retrieve_project_budget,
                                         update_project_budget, delete_project_budget)


class ProjectBudgetListResource(Resource):
    def get(self):
        return retrieve_project_budgets()

    def post(self):
        data = request.json
        return add_project_budget(data)


class ProjectBudgetResource(Resource):
    def get(self, project_budget_id):
        return retrieve_project_budget(project_budget_id)

    def put(self, project_budget_id):
        data = request.json
        return update_project_budget(project_budget_id, data)

    def delete(self, project_budget_id):
        return delete_project_budget(project_budget_id)
