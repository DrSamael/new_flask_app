from datetime import datetime, timedelta
from bson import ObjectId, errors

from source.database import projects_collection
from source.database import project_budgets_collection


def validate_customer_eligibility(customer_id):
    try:
        customer_id = ObjectId(customer_id)
    except errors.InvalidId:
        return {"error": "Invalid customer ID"}, 400

    project_ids = [project["_id"] for project in projects_collection.find({"customer_id": customer_id})]
    if not project_ids:
        return None

    three_months_ago = datetime.now() - timedelta(days=90)
    unpaid_project_budgets = list(project_budgets_collection.find({
        "project_id": {"$in": project_ids},
        "is_paid": False,
        "created_at": {"$lt": three_months_ago}
    }))

    if len(unpaid_project_budgets) > 0:
        return {"error": "Customer has unpaid projects older than 3 months. Cannot create a new project."}, 400

    return None
