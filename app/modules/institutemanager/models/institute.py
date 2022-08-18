from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Optional, Set
from enum import Enum


class Message(BaseModel):
    message: str


class Institute(BaseModel):
    userName: str = Field(..., title="Username", example="adam_kingdom")
    instituteName: str = Field(..., title="Institute Name", example="Adam")
    address: Optional[str] = Field(
        ...,
        title="Address",
        example="Gandhi Road, Near Zarebi Bazar, VileParle",
    )
    city: Optional[str] = Field(
        ..., title="Name of City", max_length=100, example="Pune"
    )
    mobileNumber: str = Field(..., title="Mobile Numbers", example="5898787878")
    emailAddress: Optional[EmailStr] = Field(
        ..., title="Email Address", example="sample@email.com"
    )
    isActive: bool = Field(..., title="Institute Status", example=True)
    isDeleted: bool = Field(..., title="Institute Deletion Status", example=True)
    about: Optional[str] = Field(
        ..., title="Institute Information", example="Description about Institute"
    )


class InstituteReturn(BaseModel):
    u_id: int = Field(..., title="Institute Id", example=1234)
    userName: str = Field(..., title="Username", example="adam_kingdom")
    instituteName: str = Field(..., title="Institute Name", example="Adam")
    address: str = Field(
        ...,
        title="Address",
        example="Gandhi Road, Near Zarebi Bazar, VileParle",
    )
    city: str = Field(..., title="Name of City", max_length=100, example="Pune")
    mobileNumber: str = Field(..., title="Phone Numbers", example="5898787878")
    emailAddress: EmailStr = Field(
        ..., title="Email Address", example="sample@email.com"
    )
    isActive: bool = Field(..., title="Institute Status", example=True)
    isDeleted: bool = Field(..., title="Institute Deletion Status", example=True)
    about: str = Field(
        ..., title="Institute Information", example="Description about Institute"
    )
    createdAt: date = Field(..., title="Registered On", example="01/01/2000")


class InstituteUpdate(BaseModel):
    u_id: Optional[int] = Field(None, title="U_ID", example=12345)
    userName: Optional[str] = Field(None, title="Username", example="adam_kingdom")
    instituteName: Optional[str] = Field(None, title="First Name", example="Adam")
    address: Optional[str] = Field(
        None,
        title="Address of Institute",
        example="Gandhi Road, Near Zarebi Bazar, VileParle",
    )
    city: Optional[str] = Field(
        None, title="Name of City", max_length=100, example="Pune"
    )
    mobileNumber: Optional[str] = Field(
        None, title="Phone Numbers", example="5898787878"
    )
    emailAddress: Optional[EmailStr] = Field(
        None, title="Email Address", example="sample@email.com"
    )
    isActive: Optional[bool] = Field(None, title="Institute Status", example=True)
    isDeleted: Optional[bool] = Field(
        None, title="Institute Deletion Status", example=True
    )
    about: Optional[str] = Field(
        None, title="Institute Information", example="Description about Institute"
    )


class InstituteDelete(BaseModel):
    status_delete: bool = Field(..., title="Institute Status", example=True)
