from marshmallow import Schema, fields


class PositionSchema(Schema):
    title = fields.String(required=True)
    coefficient = fields.Float(required=True)


class QualificationSchema(Schema):
    title = fields.String(required=True)
    pay_rate = fields.Float(required=True)


class EmployeeSchema(Schema):
    name = fields.String(required=True)
    date_of_birth = fields.String(required=False, allow_none=True)
    phone = fields.String(required=False, allow_none=True)
    is_active = fields.Boolean(missing=True)
    position = fields.Nested(PositionSchema, required=True)
    qualification = fields.Nested(QualificationSchema, required=True)


employee_schema = EmployeeSchema()
