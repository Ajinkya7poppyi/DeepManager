from datetime import date
from typing import Optional, List
from fastapi import Body, Depends, HTTPException, status, Query
from pydantic import EmailStr
from .app_helper import (
    create_attendance,
    get_attendance,
    update_attendance,
    delete_attendace,
)
from .models import (
    AttendanceReturn,
    Attendance,
    AttendanceUpdate,
    AttendanceDelete,
    UserType,
    Message,
    TokenData,
)
from fastapi import APIRouter
from ..accessmanager.app_helper import get_current_user

attendance_manager_app = APIRouter(tags=["Attendance Manager"])


@attendance_manager_app.post(
    "/attendance",
    summary="Create a new Attendance",
    description="Add a new Attendance",
    response_model=AttendanceReturn,
    response_description="Creates Attendance",
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": Message}},
    tags=["Attendance Manager"],
)
async def create_user(attendace: Attendance = Body(...)):
    try:
        response_att = create_attendance(attendance_dict=attendace.dict())
        if response_att:
            return response_att
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@attendance_manager_app.get(
    "/attendance",
    summary="Get all Attendance",
    description="Get all Attendance",
    response_model=List[AttendanceReturn],
    response_description="Get all Attendance",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Attendance Manager"],
)
async def get_user(
    current_user: TokenData = Depends(get_current_user),
    instituteId: int = Query(
        None, title="Institute Id", description="Id of The Institute", example=123
    ),
    batch_id: Optional[int] = Query(
        None, title="Batch Id", description="Id of The Batch", example=12345
    ),
    user_type: UserType = Query(
        None, title="User", description="User Type", example="student"
    ),
    attendance_date: date = Query(
        None,
        title="Attendance Date",
        description="Date of The Attendance",
        example="2020-01-01",
    ),
):
    try:
        response_att = get_attendance(
            institute_id=instituteId,
            batch_id=batch_id,
            user_type=user_type,
            attendance_date=attendance_date,
        )
        return response_att
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@attendance_manager_app.put(
    "/attendance",
    summary="Update a Attendance",
    description="Update a Attendance",
    response_model=AttendanceReturn,
    status_code=status.HTTP_202_ACCEPTED,
    responses={400: {"model": Message}},
    tags=["Attendance Manager"],
)
async def update_user(
    current_user: TokenData = Depends(get_current_user),
    attendance_id: int = Query(
        ..., title="Attendace Id", description="Id of The attendace", example=123
    ),
    batch: AttendanceUpdate = Body(...),
):
    try:
        response_att = update_attendance(
            attance_id=attendance_id, update_dict=batch.dict()
        )
        return response_att
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@attendance_manager_app.delete(
    "/attendance",
    summary="Delete a Attendace",
    description="Delete a Attendance",
    response_description="Delete Batch",
    response_model=AttendanceDelete,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Attendance Manager"],
)
async def delete_user(
    current_user: TokenData = Depends(get_current_user),
    instituteId: int = Query(
        None, title="Institute Id", description="Id of The Institute", example=123
    ),
    batch_id: Optional[int] = Query(
        None, title="Batch Id", description="Id of The Batch", example=12345
    ),
    user_type: UserType = Query(
        None, title="User", description="User Type", example="student"
    ),
    attendance_date: date = Query(
        None,
        title="Attendance Date",
        description="Date of The Attendance",
        example="2020-01-01",
    ),
):
    try:
        response_att = delete_attendace(
            institute_id=instituteId,
            batch_id=batch_id,
            user_type=user_type,
            attendance_date=attendance_date,
        )
        return {"status_delete": response_att}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
