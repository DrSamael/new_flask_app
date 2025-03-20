from marshmallow import Schema, fields


class EmployeeSchema(Schema):
    name = fields.String(required=True)
    date_of_birth = fields.String(required=False, allow_none=True)
    phone = fields.String(required=False, allow_none=True)
    is_active = fields.Boolean(missing=True)


employee_schema = EmployeeSchema()
