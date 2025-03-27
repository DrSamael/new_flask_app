from marshmallow import fields
from bson import ObjectId


def serialize_doc(doc):
    return {key: str(value) if isinstance(value, ObjectId) else value for key, value in doc.items()}


class ObjectIdField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return str(value) if isinstance(value, ObjectId) else None

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return ObjectId(value)
        except Exception:
            raise fields.ValidationError("Invalid ObjectId format.")
