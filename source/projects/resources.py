from flask_restful import Resource
from flask import request

from source.projects.crud import add_project, retrieve_projects, retrieve_project, update_project, delete_project


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
