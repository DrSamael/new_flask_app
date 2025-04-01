from source.project_budgets.resources import ProjectBudgetListResource, ProjectBudgetResource


def initialize_routes(api):
    api.add_resource(ProjectBudgetListResource, "/project-budgets")
    api.add_resource(ProjectBudgetResource, "/project-budgets/<string:project_budget_id>")
