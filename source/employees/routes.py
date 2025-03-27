from source.employees.resources import EmployeeListResource, EmployeeResource


def initialize_routes(api):
    api.add_resource(EmployeeListResource, "/employees")
    api.add_resource(EmployeeResource, "/employees/<string:employee_id>")
