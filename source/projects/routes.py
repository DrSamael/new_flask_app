from source.projects.resources import ProjectListResource, ProjectResource


def initialize_routes(api):
    api.add_resource(ProjectListResource, "/projects")
    api.add_resource(ProjectResource, "/projects/<string:project_id>")
