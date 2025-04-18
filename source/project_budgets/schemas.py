from marshmallow import Schema, fields

from source.utils import ObjectIdField


class ProjectBudgetSchema(Schema):
    monthly_payment = fields.Float(required=True)
    is_paid = fields.Boolean(missing=False)
    project_id = ObjectIdField(required=True)
    created_at = fields.DateTime(dump_only=True)


project_budget_schema = ProjectBudgetSchema()
