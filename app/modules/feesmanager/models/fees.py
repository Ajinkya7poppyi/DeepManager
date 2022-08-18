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


class Fees(BaseModel):
    instituteId: int = Field(..., title="Institute ID", example=123)
    userType: UserType = Field(..., title="User Type", example=UserType.institute)
    userId: int = Field(..., title="User ID", example=123)
    batchId: int = Field(..., title="Batch ID", example=123)
    amount: int = Field(..., title="Amount", example=100)
    transactionDetails: str = Field(
        ..., title="Transaction Details", example="Payment for training"
    )


class FeesReturn(BaseModel):
    u_id: int = Field(..., title="Fee Payment Id", example=1234)
    instituteId: int = Field(..., title="Institute ID", example=123)
    userType: UserType = Field(..., title="User Type", example=UserType.institute)
    userId: int = Field(..., title="User ID", example=123)
    batchId: int = Field(..., title="Batch ID", example=123)
    amount: int = Field(..., title="Amount", example=100)
    transactionDetails: str = Field(
        ..., title="Transaction Details", example="Payment for training"
    )
    createdAt: date = Field(..., title="Fees Paid On", example="01/01/2000")


class FeesUpdate(BaseModel):
    u_id: Optional[int] = Field(None, title="Fee Payment Id", example=12345)
    instituteId: Optional[int] = Field(None, title="Institute ID", example=123)
    userType: Optional[UserType] = Field(
        None, title="User Type", example=UserType.institute
    )
    userId: Optional[int] = Field(None, title="User ID", example=123)
    batchId: int = Field(..., title="Batch ID", example=123)
    amount: int = Field(..., title="Amount", example=100)
    transactionDetails: str = Field(
        ..., title="Transaction Details", example="Payment for training"
    )


class FeesDelete(BaseModel):
    status_delete: bool = Field(..., title="Fees Status", example=True)
