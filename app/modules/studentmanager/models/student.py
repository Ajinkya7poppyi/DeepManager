from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Optional, Set
from enum import Enum


class UserType(str, Enum):
    """UserType"""

    institute = "Institute"
    trainer = "Trainer"
    student = "Student"


class Gender(str, Enum):
    M = "Male"
    F = "Female"
    I = "Intersex"


class Message(BaseModel):
    message: str


class Student(BaseModel):
    instituteId: int = Field(..., title="Institute Id", example=12345)
    userType: UserType = Field(..., title="User Category", example="Trainer")
    userName: str = Field(..., title="Username", example="adam_kingdom")
    firstName: str = Field(..., title="First Name", example="Adam")
    middleName: str = Field(..., title="Middle Name", example="Stewart")
    lastName: str = Field(..., title="Last Name", example="Kallis")
    birthDate: date = Field(..., title="Birth Date", example="YYYY-MM-DD")
    gender: Gender = Field(..., title="Gender", example="Male")
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
    isActive: bool = Field(..., title="Student Status", example=True)
    isDeleted: bool = Field(..., title="Student Deletion Status", example=True)
    batches: Optional[Set[str]] = Field(
        ..., title="Batches", example={"Mor-1245", "Eve-1245"}
    )
    about: Optional[str] = Field(
        ..., title="Student Information", example="Description about Student"
    )

    class Config:
        use_enum_values = True


class StudentReturn(BaseModel):
    u_id: int = Field(..., title="Student Id", example=1234)
    instituteId: int = Field(..., title="Institute Id", example=1234)
    firstName: str = Field(..., title="First Name", example="Adam")
    middleName: str = Field(..., title="Middle Name", example="Stewart")
    lastName: str = Field(..., title="Last Name", example="Kallis")
    birthDate: date = Field(..., title="Birth Date", example="01/01/2000")
    age: int = Field(..., title="Age", example=20)
    gender: Gender = Field(..., title="Gender", example="Male")
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
    isActive: bool = Field(..., title="Student Status", example=True)
    isDeleted: bool = Field(..., title="Student Deletion Status", example=True)
    batches: Set[str] = Field(..., title="Batches", example={"Mor-1245", "Eve-1245"})
    about: str = Field(
        ..., title="Student Information", example="Description about Student"
    )
    createdAt: date = Field(..., title="Registered On", example="01/01/2000")

    class Config:
        use_enum_values = True


class StudentUpdate(BaseModel):
    u_id: Optional[int] = Field(None, title="U_ID", example=1234)
    instituteId: Optional[int] = Field(None, title="Institute Id", example=1234)
    userType: Optional[UserType] = Field(None, title="User Category", example="Trainer")
    userName: Optional[str] = Field(None, title="Username", example="adam_kingdom")
    firstName: Optional[str] = Field(None, title="First Name", example="Adam")
    middleName: Optional[str] = Field(None, title="Middle Name", example="Stewart")
    lastName: Optional[str] = Field(None, title="Last Name", example="Kallis")
    birthDate: Optional[date] = Field(None, title="Birth Date", example="01/01/2000")
    gender: Optional[Gender] = Field(None, title="Gender", example="Male")
    address: Optional[str] = Field(
        None,
        title="Address of Student",
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
    isActive: Optional[bool] = Field(None, title="Student Status", example=True)
    isDeleted: Optional[bool] = Field(
        None, title="Student Deletion Status", example=True
    )
    batches: Optional[Set[str]] = Field(
        None, title="Batches", example={"Mor-1245", "Eve-1245"}
    )
    about: Optional[str] = Field(
        None, title="Student Information", example="Description about Student"
    )

    class Config:
        use_enum_values = True


class StudentDelete(BaseModel):
    status_delete: bool = Field(..., title="Student Status", example=True)
