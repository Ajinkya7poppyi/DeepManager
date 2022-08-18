from typing_extensions import Required
from mongoengine.document import Document
from mongoengine.fields import (
    IntField,
    StringField,
    DateTimeField,
    UUIDField,
    EmailField,
)


class User(Document):
    """User Credtinal Model"""

    u_id = IntField(required=True, unique=True)
    userName = StringField(required=True, unique=True)
    userPassword = StringField(required=True)
    userType = StringField(required=True)
    emailAddress = EmailField(required=True, unique=True)
    mobileNumber = StringField(required=True, unique=True)
    createdAt = DateTimeField(auto_now_add=True, auto_now_on_update=False)
    updatedAt = DateTimeField(auto_now_add=True, auto_now_on_update=True)
