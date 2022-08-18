from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Set


class Message(BaseModel):
    message: str


class Batch(BaseModel):
    instituteId: int = Field(..., title="Institute Id", example=12345)
    batchName: str = Field(..., title="Username", example="adam_kingdom")
    students: Optional[Set[int]] = Field(..., title="Students", example=[1, 2, 3])
    trainers: Optional[Set[int]] = Field(..., title="Trainers", example=[1, 2, 3])
    isActive: bool = Field(..., title="Batch Status", example=True)
    isDeleted: bool = Field(..., title="Batch Deletion Status", example=True)
    about: Optional[str] = Field(
        ..., title="Batch Information", example="Description about Batch"
    )


class BatchReturn(BaseModel):
    u_id: int = Field(..., title="Batch Id", example=12345)
    instituteId: int = Field(..., title="Institute Id", example=12345)
    batchName: str = Field(..., title="Username", example="adam_kingdom")
    students: Optional[Set[int]] = Field(..., title="Students", example=[1, 2, 3])
    trainers: Optional[Set[int]] = Field(..., title="Trainers", example=[1, 2, 3])
    isActive: bool = Field(..., title="Batch Status", example=True)
    isDeleted: bool = Field(..., title="Batch Deletion Status", example=True)
    about: Optional[str] = Field(
        ..., title="Batch Information", example="Description about Batch"
    )
    createdAt: date = Field(..., title="Registered On", example="01/01/2000")


class BatchUpdate(BaseModel):
    u_id: int = Field(..., title="Batch Id", example=12345)
    instituteId: Optional[int] = Field(..., title="Institute Id", example=12345)
    batchName: Optional[str] = Field(..., title="Username", example="adam_kingdom")
    students: Optional[Set[int]] = Field(..., title="Students", example=[1, 2, 3])
    trainers: Optional[Set[int]] = Field(..., title="Trainers", example=[1, 2, 3])
    isActive: Optional[bool] = Field(..., title="Batch Status", example=True)
    isDeleted: Optional[bool] = Field(..., title="Batch Deletion Status", example=True)
    about: Optional[str] = Field(
        ..., title="Batch Information", example="Description about Batch"
    )


class BatchDelete(BaseModel):
    status_delete: bool = Field(..., title="Batch Status", example=True)
