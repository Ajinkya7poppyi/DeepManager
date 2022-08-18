from typing import Optional, List
from fastapi import Body, Depends, HTTPException, status, Query
from pydantic import EmailStr
from .app_helper import (
    create_trainer,
    delete_trainer,
    get_trainer,
    update_trainer,
)
from .models import (
    Trainer,
    TrainerReturn,
    TrainerUpdate,
    TrainerDelete,
    Message,
    TokenData,
)
from fastapi import APIRouter
from ..accessmanager.app_helper import get_current_user

trainer_manager_app = APIRouter(tags=["Trainer Manager"])


@trainer_manager_app.post(
    "/trainer",
    summary="Create a new Trainer",
    description="Add a new Trainer",
    response_model=TrainerReturn,
    response_description="Creates Trainer",
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": Message}},
    tags=["Trainer Manager"],
)
async def create_user(user: Trainer = Body(...)):
    try:
        response_usr = create_trainer(user.dict())
        if response_usr:
            return response_usr
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@trainer_manager_app.get(
    "/trainer",
    summary="Get all Trainer",
    description="Get all Trainer",
    response_model=List[TrainerReturn],
    response_description="Get all Trainer",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Trainer Manager"],
)
async def get_user(
    current_user: TokenData = Depends(get_current_user),
    instituteId: int = Query(
        None, title="Institute Id", description="Id of The Institute", example="I-123"
    ),
    u_id: Optional[int] = Query(
        None, title="Trainer Id", description="Id of The Trainer", example="123"
    ),
    userName: Optional[str] = Query(
        None,
        title="Trainer Name",
        description="UserName of The Trainer",
        example="adam_sit",
    ),
    emailAddress: Optional[EmailStr] = Query(
        None,
        title="Email of Trainer",
        description="Email of Trainer",
        example="dd@testemail.com",
    ),
    mobileNumber: Optional[str] = Query(
        None,
        title="Mobile number of Trainer",
        description="Mobile of The Trainer",
        example="+91-9028077584",
    ),
):
    try:
        response_usr = get_trainer(
            institute_id=instituteId,
            u_id=u_id,
            username=userName,
            email=emailAddress,
            mobile=mobileNumber,
        )
        return response_usr
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@trainer_manager_app.put(
    "/trainer",
    summary="Update a Trainer",
    description="Update a Trainer",
    response_model=TrainerReturn,
    status_code=status.HTTP_202_ACCEPTED,
    responses={400: {"model": Message}},
    tags=["Trainer Manager"],
)
async def update_user(
    current_user: TokenData = Depends(get_current_user),
    u_id: int = Query(
        ..., title="User Id", description="Id of The user", example="123"
    ),
    user: TrainerUpdate = Body(...),
):
    try:
        response_inst = update_trainer(u_id, user.dict())
        return response_inst
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@trainer_manager_app.delete(
    "/trainer",
    summary="Delete a Trainer",
    description="Delete a Trainer",
    response_description="Delete Trainer",
    response_model=TrainerDelete,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Trainer Manager"],
)
async def delete_user(
    current_user: TokenData = Depends(get_current_user),
    instituteId: int = Query(
        None, title="Institute Id", description="Id of The Institute", example="I-123"
    ),
    u_id: Optional[int] = Query(
        None, title="Trainer Id", description="Id of The Trainer", example="T-123"
    ),
    userName: Optional[str] = Query(
        None,
        title="Trainer Name",
        description="UserName of The Trainer",
        example="adam_sit",
    ),
    emailAddress: Optional[EmailStr] = Query(
        None,
        title="Email of Trainer",
        description="Email of The Trainer",
        example="dd@testemail.com",
    ),
    mobileNumber: Optional[str] = Query(
        None,
        title="Mobile number of Trainer",
        description="Mobile of The Trainer",
        example="+91-9028077584",
    ),
):
    try:
        response_usr = delete_trainer(
            institute_id=instituteId,
            u_id=u_id,
            username=userName,
            email=emailAddress,
            mobile=mobileNumber,
        )
        return {"status_delete": response_usr}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
