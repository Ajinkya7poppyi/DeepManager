from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from enum import Enum


class UserType(str, Enum):
    """UserType"""

    institute = "Institute"
    trainer = "Trainer"
    student = "Student"


class User(BaseModel):
    """User Model"""

    u_id: int = Field(..., title="User Id", example=1234)
    userName: str = Field(..., title="Username", example="adam_kingdom")
    userType: UserType = Field(..., title="User Category", example="Trainer")
    emailAddress: EmailStr = Field(
        ..., title="Email Address", example="sample@email.com"
    )
    mobileNumber: str = Field(..., title="Mobile Number", example="+919123456789")
    userPassword: str = Field(..., title="User Password", example="*************")

    class Config:
        use_enum_values = True


class UserReturn(BaseModel):
    """User Return"""

    u_id: int = Field(..., title="User Id", example=1234)
    userName: str = Field(..., title="Username", example="adam_kingdom")
    userType: str = Field(..., title="User Category", example="Trainer")
    emailAddress: EmailStr = Field(
        ..., title="Email Address", example="sample@email.com"
    )
    mobileNumber: str = Field(..., title="Mobile Number", example="+91-9123456789")


class UserUpdate(BaseModel):
    """User Update Model"""

    userName: Optional[str] = Field(None, title="Username", example="adam_kingdom")
    userType: Optional[UserType] = Field(None, title="User Category", example="Trainer")
    emailAddress: Optional[EmailStr] = Field(
        None, title="Email Address", example="sample@email.com"
    )
    userPassword: Optional[str] = Field(
        None, title="User Password", example="*************"
    )
    mobileNumber: Optional[str] = Field(
        None, title="Mobile Number", example="+919123456789"
    )

    class Config:
        use_enum_values = True


class UserDelete(BaseModel):
    """User Delete Model"""

    status_delete: bool = Field(..., title="User Status", example=True)


class Message(BaseModel):
    """Exception Message"""

    message: str
