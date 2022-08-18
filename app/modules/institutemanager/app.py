from typing import Optional, List
from fastapi import Body, Depends, HTTPException, status, Query
from pydantic import EmailStr
from .app_helper import (
    create_institute,
    get_institute,
    update_institute,
    delete_institute,
)
from .models import (
    Institute,
    InstituteUpdate,
    InstituteReturn,
    InstituteDelete,
    Message,
    TokenData,
)
from fastapi import APIRouter
from ..accessmanager.app_helper import get_current_user

institute_manager_app = APIRouter(tags=["Institute Manager"])


@institute_manager_app.post(
    "/institute",
    summary="Create a new Institute",
    description="Add a new Institute",
    response_model=InstituteReturn,
    response_description="Creates Institute",
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": Message}},
    tags=["Institute Manager"],
)
async def create_user(user: Institute = Body(...)):
    try:
        response_inst = create_institute(user.dict())
        if response_inst:
            return response_inst
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@institute_manager_app.get(
    "/institute",
    summary="Get all Institute",
    description="Get all Institute",
    response_model=List[InstituteReturn],
    response_description="Get all Institute",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Institute Manager"],
)
async def get_user(
    current_user: TokenData = Depends(get_current_user),
    u_id: Optional[int] = Query(
        None, title="Institute Id", description="Id of The Institute", example="123"
    ),
    userName: Optional[str] = Query(
        None,
        title="Institute Name",
        description="UserName of The StInstituteudent",
        example="adam_sit",
    ),
    emailAddress: Optional[EmailStr] = Query(
        None,
        title="Email of Institute",
        description="Email of Institute",
        example="dd@testemail.com",
    ),
    mobileNumber: Optional[str] = Query(
        None,
        title="Mobile number of Institute",
        description="Mobile of The Institute",
        example="+91-9028077584",
    ),
):
    try:
        response_inst = get_institute(
            u_id=u_id,
            username=userName,
            email=emailAddress,
            mobile=mobileNumber,
        )
        return response_inst
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@institute_manager_app.put(
    "/institute",
    summary="Update a Institute",
    description="Update a Institute",
    response_model=InstituteReturn,
    status_code=status.HTTP_202_ACCEPTED,
    responses={400: {"model": Message}},
    tags=["Institute Manager"],
)
async def update_user(
    current_user: TokenData = Depends(get_current_user),
    u_id: int = Query(
        ..., title="User Id", description="Id of The Institute", example="123"
    ),
    institute: InstituteUpdate = Body(...),
):
    try:
        response_inst = update_institute(u_id, institute.dict())
        return response_inst
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@institute_manager_app.delete(
    "/institute",
    summary="Delete a Institute",
    description="Delete a Institute",
    response_description="Delete Institute",
    response_model=InstituteDelete,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Institute Manager"],
)
async def delete_user(
    current_user: TokenData = Depends(get_current_user),
    u_id: Optional[int] = Query(
        None, title="Institute Id", description="Id of The Institute", example="T-123"
    ),
    userName: Optional[str] = Query(
        None,
        title="Institute Name",
        description="UserName of The Institute",
        example="adam_sit",
    ),
    emailAddress: Optional[EmailStr] = Query(
        None,
        title="Email of Student",
        description="Email of The Institute",
        example="dd@testemail.com",
    ),
    mobileNumber: Optional[str] = Query(
        None,
        title="Mobile number of Institute",
        description="Mobile of The Institute",
        example="+91-9028077584",
    ),
):
    try:
        response_inst = delete_institute(
            u_id=u_id,
            username=userName,
            email=emailAddress,
            mobile=mobileNumber,
        )
        return {"status_delete": response_inst}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
