from typing import Optional, List
from fastapi import Body, Depends, HTTPException, status, Query
from pydantic import EmailStr
from .app_helper import (
    create_student,
    get_student,
    update_student,
    delete_student,
)
from .models import (
    Student,
    StudentDelete,
    StudentUpdate,
    StudentReturn,
    Message,
    TokenData,
)
from fastapi import APIRouter
from ..accessmanager.app_helper import get_current_user

student_manager_app = APIRouter(tags=["Student Manager"])


@student_manager_app.post(
    "/student",
    summary="Create a new Student",
    description="Add a new Student",
    response_model=StudentReturn,
    response_description="Creates Student",
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": Message}},
    tags=["Student Manager"],
)
async def create_user(user: Student = Body(...)):
    try:
        response_usr = create_student(user.dict())
        if response_usr:
            return response_usr
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_manager_app.get(
    "/student",
    summary="Get all Students",
    description="Get all Students",
    response_model=List[StudentReturn],
    response_description="Get all Students",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Student Manager"],
)
async def get_user(
    current_user: TokenData = Depends(get_current_user),
    instituteId: int = Query(
        None, title="Institute Id", description="Id of The Institute", example=12345
    ),
    u_id: Optional[int] = Query(
        None, title="Student Id", description="Id of The Student", example=12345
    ),
    userName: Optional[str] = Query(
        None,
        title="Student Name",
        description="UserName of The Student",
        example="adam_sit",
    ),
    emailAddress: Optional[EmailStr] = Query(
        None,
        title="Email of Student",
        description="Email of Student",
        example="dd@testemail.com",
    ),
    mobileNumber: Optional[str] = Query(
        None,
        title="Mobile number of Student",
        description="Mobile of The Student",
        example="+91-9028077584",
    ),
):
    try:
        response_usr = get_student(
            institute_id=instituteId,
            u_id=u_id,
            username=userName,
            email=emailAddress,
            mobile=mobileNumber,
        )
        return response_usr
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_manager_app.put(
    "/student",
    summary="Update a Student",
    description="Update a Student",
    response_model=StudentReturn,
    status_code=status.HTTP_202_ACCEPTED,
    responses={400: {"model": Message}},
    tags=["Student Manager"],
)
async def update_user(
    current_user: TokenData = Depends(get_current_user),
    u_id: int = Query(..., title="User Id", description="Id of The user", example=123),
    user: StudentUpdate = Body(...),
):
    try:
        response_inst = update_student(u_id, user.dict())
        return response_inst
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@student_manager_app.delete(
    "/student",
    summary="Delete a Student",
    description="Delete a Student",
    response_description="Delete Student",
    response_model=StudentDelete,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Student Manager"],
)
async def delete_user(
    current_user: TokenData = Depends(get_current_user),
    instituteId: int = Query(
        None, title="Institute Id", description="Id of The Institute", example=1234
    ),
    u_id: Optional[int] = Query(
        None, title="Student Id", description="Id of The Student", example=1234
    ),
    userName: Optional[str] = Query(
        None,
        title="Student Name",
        description="UserName of The Student",
        example="adam_sit",
    ),
    emailAddress: Optional[EmailStr] = Query(
        None,
        title="Email of Student",
        description="Email of The Student",
        example="dd@testemail.com",
    ),
    mobileNumber: Optional[str] = Query(
        None,
        title="Mobile number of Student",
        description="Mobile of The Student",
        example="+91-9028077584",
    ),
):
    try:
        response_usr = delete_student(
            institute_id=instituteId,
            u_id=u_id,
            username=userName,
            email=emailAddress,
            mobile=mobileNumber,
        )
        return {"status_delete": response_usr}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
