from marshmallow import Schema, fields

from source.utils import ObjectIdField


class CategorySchema(Schema):
    title = fields.String(required=True)
    coefficient = fields.Float(required=True)


class ProjectSchema(Schema):
    title = fields.String(required=True)
    start_date = fields.DateTime(required=True, format='%Y-%m-%d')
    execution_period = fields.Float(required=True)
    customer_id = ObjectIdField(required=True)
    category = fields.Nested(CategorySchema, required=True)


project_schema = ProjectSchema()
