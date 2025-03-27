from flask_restful import Resource
from flask import request

from source.customers.crud import add_customer, retrieve_customers, retrieve_customer, update_customer, delete_customer


class CustomerListResource(Resource):
    def get(self):
        return retrieve_customers()

    def post(self):
        data = request.json
        return add_customer(data)


class CustomerResource(Resource):
    def get(self, customer_id):
        return retrieve_customer(customer_id)

    def put(self, customer_id):
        data = request.json
        return update_customer(customer_id, data)

    def delete(self, customer_id):
        return delete_customer(customer_id)
