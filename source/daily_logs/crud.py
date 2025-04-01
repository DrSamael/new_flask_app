from datetime import datetime

from bson.objectid import ObjectId

from source.database import daily_logs_collection
from source.daily_logs.schemas import daily_log_schema
from source.utils import serialize_doc
from source.daily_logs.validations.daily_time_validator import validate_daily_log


def add_daily_log(data):
    validation_error = validate_daily_log(data)
    if validation_error:
        return validation_error  # Return validation error response

    daily_log = daily_log_schema.load(data)
    daily_log["created_at"] = datetime.now()
    daily_log_id = daily_logs_collection.insert_one(daily_log).inserted_id

    new_daily_log = daily_logs_collection.find_one({"_id": daily_log_id})
    return serialize_doc(new_daily_log)


def retrieve_daily_logs(statement: dict = None):
    if statement is None:
        statement = {}
    daily_logs = daily_logs_collection.find(statement)
    return [serialize_doc(emp) for emp in daily_logs]


def retrieve_daily_log(daily_log_id):
    daily_log = daily_logs_collection.find_one({"_id": ObjectId(daily_log_id)})
    if not daily_log:
        return {"error": "Daily Log not found"}, 404
    return serialize_doc(daily_log)


def update_daily_log(daily_log_id, data):
    result = daily_logs_collection.update_one({"_id": ObjectId(daily_log_id)}, {"$set": data})
    if result.matched_count == 0:
        return {"error": "Daily Log not found"}, 404

    updated_daily_log = daily_logs_collection.find_one({"_id": ObjectId(daily_log_id)})
    return serialize_doc(updated_daily_log)


def delete_daily_log(daily_log_id):
    result = daily_logs_collection.delete_one({"_id": ObjectId(daily_log_id)})
    if result.deleted_count == 0:
        return {"error": "Daily Log not found"}, 404
    return {"message": "Daily Log deleted"}
