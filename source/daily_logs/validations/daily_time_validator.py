from datetime import datetime

from bson.objectid import ObjectId

from source.database import daily_logs_collection
from source.daily_logs.schemas import daily_log_schema


def validate_daily_log(data):
    errors = daily_log_schema.validate(data)
    if errors:
        return {"error": errors}, 400

    try:
        employee_id = ObjectId(data["employee_id"])
    except:
        return {"error": "Invalid employee ID"}, 400

    execution_time = data.get("execution_time", 0)
    if execution_time <= 0:
        return {"error": "Execution time must be greater than 0"}, 400

    log_date = datetime.now()

    existing_logs = daily_logs_collection.find({
        "employee_id": employee_id,
        "created_at": {"$gte": datetime.combine(log_date, datetime.min.time()),
                       "$lt": datetime.combine(log_date, datetime.max.time())}
    })

    total_hours_today = sum(log["execution_time"] for log in existing_logs)
    if total_hours_today + execution_time > 10:
        return {"error": "Daily limit exceeded. Cannot log more than 10 hours per day."}, 400

    return None
