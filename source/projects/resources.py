from flask_restful import Resource
from flask import request

from source.projects.crud import add_project, retrieve_projects, retrieve_project, update_project, delete_project
from source.projects.services.calculate_project_monthly_report import calculate_project_monthly_report


class ProjectListResource(Resource):
    def get(self):
        return retrieve_projects()

    def post(self):
        data = request.json
        return add_project(data)


class ProjectResource(Resource):
    def get(self, project_id):
        return retrieve_project(project_id)

    def put(self, project_id):
        data = request.json
        return update_project(project_id, data)

    def delete(self, project_id):
        return delete_project(project_id)


class ProjectReportResource(Resource):
    def get(self, project_id):
        month = request.args.get("month", type=int)
        year = request.args.get("year", type=int)

        if not month or not year:
            return {"error": "month and year parameters are required"}, 400

        return calculate_project_monthly_report(project_id, month, year)
