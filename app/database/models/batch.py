import datetime
from mongoengine.document import Document
from mongoengine.fields import (
    BooleanField,
    StringField,
    DateTimeField,
    IntField,
    ListField,
)


class Batch(Document):
    """Batch Model"""

    u_id = IntField()
    instituteId = IntField()
    batchName = StringField(unique=True, max_length=100)
    students = ListField(IntField())
    trainers = ListField(IntField())
    isActive = BooleanField()
    isDeleted = BooleanField()
    about = StringField()
    createdAt = DateTimeField(default=datetime.datetime.utcnow)
    updatedAt = DateTimeField()
