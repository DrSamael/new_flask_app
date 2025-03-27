from marshmallow import Schema, fields


class CustomerSchema(Schema):
    title = fields.String(required=True)


customer_schema = CustomerSchema()
