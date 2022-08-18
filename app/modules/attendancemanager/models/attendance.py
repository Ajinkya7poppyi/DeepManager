from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Set
from enum import Enum


class UserType(str, Enum):
    """UserType"""

    institute = "Institute"
    trainer = "Trainer"
    student = "Student"


class Message(BaseModel):
    message: str


class Attendance(BaseModel):
    instituteId: int = Field(..., title="Institute Id", example=12345)
    batchId: int = Field(..., title="BatchId", example=12345)
    userType: UserType = Field(..., title="UserType", example=UserType.student)
    attendaceDate: date = Field(..., title="Attendance Date", example=date.today())
    presentIds: Set[int] = Field(..., title="PresentIds", example={1, 2, 3})


class AttendanceReturn(BaseModel):
    u_id: int = Field(..., title="Attence Id", example=12345)
    instituteId: int = Field(..., title="Institute Id", example=12345)
    batchId: int = Field(..., title="BatchId", example=12345)
    userType: UserType = Field(..., title="UserType", example=UserType.student)
    attendaceDate: date = Field(..., title="Attendance Date", example=date.today())
    presentIds: Set[int] = Field(..., title="PresentIds", example={1, 2, 3})
    createdAt: date = Field(..., title="Registered On", example="01/01/2000")


class AttendanceUpdate(BaseModel):
    u_id: Optional[int] = Field(..., title="Attence Id", example=12345)
    instituteId: Optional[int] = Field(..., title="Institute Id", example=12345)
    batchId: Optional[int] = Field(..., title="BatchId", example=12345)
    userType: Optional[UserType] = Field(
        ..., title="UserType", example=UserType.student
    )
    attendaceDate: Optional[date] = Field(
        ..., title="Attendance Date", example=date.today()
    )
    presentIds: Optional[Set[int]] = Field(..., title="PresentIds", example={1, 2, 3})


class AttendanceDelete(BaseModel):
    status_delete: bool = Field(..., title="Attence Status", example=True)
