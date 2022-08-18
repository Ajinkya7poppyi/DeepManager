import datetime
from typing_extensions import Required
from mongoengine.document import Document
from mongoengine.fields import (
    StringField,
    DateField,
    DateTimeField,
    IntField,
    ListField,
)


class Attendance(Document):
    """Attendance Model"""

    u_id = DateField()
    instituteId = IntField()
    batchId = IntField()
    userType = StringField()
    presentIds = ListField(IntField())
    createdAt = DateTimeField(default=datetime.datetime.utcnow)
    updatedAt = DateTimeField()
