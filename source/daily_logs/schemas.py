from marshmallow import Schema, fields

from source.utils import ObjectIdField


class DailyLogSchema(Schema):
    description = fields.String(required=True)
    execution_time = fields.Float(required=True)
    project_id = ObjectIdField(required=True)
    employee_id = ObjectIdField(required=True)
    created_at = fields.DateTime(dump_only=True)


daily_log_schema = DailyLogSchema()
