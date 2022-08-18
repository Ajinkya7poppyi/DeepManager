import datetime
from typing_extensions import Required
from mongoengine.document import Document
from mongoengine.fields import (
    BooleanField,
    StringField,
    DateTimeField,
    IntField,
    EmailField,
    ListField,
)


class Student(Document):
    """Student Model"""

    u_id = IntField()
    instituteId = IntField()
    userName = StringField(unique=True, max_length=100)
    userType = StringField()
    firstName = StringField(max_length=100)
    middleName = StringField(max_length=100)
    lastName = StringField(max_length=100)
    birthDate = DateTimeField()
    mobileNumber = StringField(min_length=9, max_length=15)
    age = IntField(max_value=130)
    gender = StringField()
    address = StringField()
    city = StringField()
    emailAddress = EmailField(unique=True)
    isActive = BooleanField()
    isDeleted = BooleanField()
    about = StringField()
    createdAt = DateTimeField(default=datetime.datetime.utcnow)
    updatedAt = DateTimeField()
