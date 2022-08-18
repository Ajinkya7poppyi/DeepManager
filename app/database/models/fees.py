import datetime
from typing_extensions import Required
from mongoengine.document import Document
from mongoengine.fields import (
    StringField,
    DateTimeField,
    IntField,
)


class Fees(Document):
    """Fees Model"""

    u_id = IntField()
    instituteId = IntField()
    userType = StringField()
    userId = IntField()
    batchId = IntField()
    amount = IntField()
    transactionDetails = StringField()
    createdAt = DateTimeField(default=datetime.datetime.utcnow)
    updatedAt = DateTimeField()
