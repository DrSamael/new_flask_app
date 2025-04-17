import pandas as pd

from source.employees.schemas import employee_schema
from source.employees.crud import add_employee


def import_employees(file):
    try:
        df = pd.read_csv(file)
    except Exception as e:
        return {"error": f"Failed to read CSV: {str(e)}"}, 400

    created = []
    failed = []

    for index, row in df.iterrows():
        employee_data = form_employee_data(row)

        errors = employee_schema.validate(employee_data)
        if errors:
            failed.append({"row": index + 1, "errors": errors})
            continue

        try:
            add_employee(employee_data)
            created.append(employee_data["name"])
        except Exception as e:
            failed.append({"row": index + 1, "error": str(e)})

    return {"success_count": len(created), "fail_count": len(failed), "created": created, "failed": failed}


def form_employee_data(row):
    return {
        "name": row.get("name"),
        "date_of_birth": row.get("date_of_birth"),
        "phone": str(row.get("phone")),
        "is_active": row.get("is_active", True),
        "position": {
            "title": row.get("position_title"),
            "coefficient": row.get("position_coefficient")
        },
        "qualification": {
            "title": row.get("qualification_title"),
            "pay_rate": row.get("qualification_pay_rate")
        }
    }
