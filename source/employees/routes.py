from source.employees.resources import (EmployeeListResource, EmployeeResource, EmployeeWageResource,
                                        EmployeeAllWageResource)


def initialize_routes(api):
    api.add_resource(EmployeeListResource, "/employees")
    api.add_resource(EmployeeResource, "/employees/<string:employee_id>")
    api.add_resource(EmployeeWageResource, "/employees/<string:employee_id>/wages")
    api.add_resource(EmployeeAllWageResource, "/employees/wages")
