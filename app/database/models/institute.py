import datetime
from typing_extensions import Required
from mongoengine.document import Document
from mongoengine.fields import (
    BooleanField,
    ListField,
    StringField,
    DateTimeField,
    IntField,
    EmailField,
)


class Institute(Document):
    """Institute Model"""

    u_id = IntField()
    userName = StringField(unique=True, max_length=100)
    instituteName = StringField(max_length=100)
    mobileNumber = StringField(min_length=9, max_length=15)
    address = StringField(max_length=200)
    city = StringField(max_length=100)
    emailAddress = EmailField(unique=True, max_length=100)
    isActive = BooleanField()
    isDeleted = BooleanField()
    about = StringField(max_length=500)
    createdAt = DateTimeField(default=datetime.datetime.utcnow)
    updatedAt = DateTimeField()
