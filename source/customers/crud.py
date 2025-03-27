from bson.objectid import ObjectId

from source.database import customers_collection
from source.customers.schemas import customer_schema
from source.utils import serialize_doc


def add_customer(data):
    errors = customer_schema.validate(data)
    if errors:
        return {"error": errors}, 400

    customer = customer_schema.load(data)
    customer_id = customers_collection.insert_one(customer).inserted_id

    new_customer = customers_collection.find_one({"_id": customer_id})
    return serialize_doc(new_customer)


def retrieve_customers():
    customers = customers_collection.find()
    return [serialize_doc(customer) for customer in customers]


def retrieve_customer(customer_id):
    customer = customers_collection.find_one({"_id": ObjectId(customer_id)})
    if not customer:
        return {"error": "Customer not found"}, 404
    return serialize_doc(customer)


def update_customer(customer_id, data):
    result = customers_collection.update_one({"_id": ObjectId(customer_id)}, {"$set": data})
    if result.matched_count == 0:
        return {"error": "Customer not found"}, 404

    updated_customer = customers_collection.find_one({"_id": ObjectId(customer_id)})
    return serialize_doc(updated_customer)


def delete_customer(customer_id):
    result = customers_collection.delete_one({"_id": ObjectId(customer_id)})
    if result.deleted_count == 0:
        return {"error": "Customer not found"}, 404
    return {"message": "Customer deleted"}
