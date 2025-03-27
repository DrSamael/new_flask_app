from source.customers.resources import CustomerListResource, CustomerResource


def initialize_routes(api):
    api.add_resource(CustomerListResource, "/customers")
    api.add_resource(CustomerResource, "/customers/<string:customer_id>")
