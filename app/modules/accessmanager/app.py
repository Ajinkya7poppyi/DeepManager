from datetime import timedelta
from typing import Optional, List
from fastapi import Body, Depends, HTTPException, status, Query
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from pydantic import EmailStr

from ..utils import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from .app_helper import (
    create_users,
    get_current_user,
    update_users,
    delete_users,
    get_users,
    authenticate_user,
)
from .models import (
    User,
    UserUpdate,
    UserReturn,
    UserDelete,
    Message,
    TokenData,
    Token,
)
from fastapi import APIRouter

access_manager_app = APIRouter(tags=["Access Manager"])


@access_manager_app.post(
    "/user",
    summary="Create a new User",
    description="Add a new user",
    response_model=UserReturn,
    response_description="Creates User Type",
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": Message}},
    tags=["Access Manager"],
)
async def create_user(user: User = Body(...)):
    try:
        response_usr = create_users(user.dict())
        if response_usr:
            return response_usr
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@access_manager_app.get(
    "/user",
    summary="Get all Users",
    description="Get all Users",
    response_model=List[UserReturn],
    response_description="Get all Users",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Access Manager"],
)
async def get_user(
    current_user: TokenData = Depends(get_current_user),
    u_id: Optional[int] = Query(
        None, title="User Id", description="Id of The user", example="123"
    ),
    userName: Optional[str] = Query(
        None, title="User Name", description="UserName of The user", example="adam_sit"
    ),
    emailAddress: Optional[EmailStr] = Query(
        None,
        title="Email of user",
        description="Email of The user",
        example="dd@testemail.com",
    ),
    mobileNumber: Optional[str] = Query(
        None,
        title="Mobile number of user",
        description="Mobile of The user",
        example="+91-9028077584",
    ),
):
    try:
        response_usr = get_users(
            u_id=u_id, username=userName, email=emailAddress, mobile=mobileNumber
        )
        return response_usr
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@access_manager_app.put(
    "/user",
    summary="Update a User",
    description="Update a User",
    response_model=UserReturn,
    status_code=status.HTTP_202_ACCEPTED,
    responses={400: {"model": Message}},
    tags=["Access Manager"],
)
async def update_user(
    current_user: TokenData = Depends(get_current_user),
    u_id: int = Query(
        ..., title="User Id", description="Id of The user", example="123"
    ),
    user: UserUpdate = Body(...),
):
    try:
        response_inst = update_users(u_id, user.dict())
        return response_inst
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@access_manager_app.delete(
    "/user",
    summary="Delete a User",
    description="Delete a User",
    response_description="Delete user",
    response_model=UserDelete,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Access Manager"],
)
async def delete_user(
    current_user: TokenData = Depends(get_current_user),
    u_id: Optional[int] = Query(
        None, title="User Id", description="Id of The user", example="T-123"
    ),
    userName: Optional[str] = Query(
        None, title="User Name", description="UserName of The user", example="adam_sit"
    ),
    emailAddress: Optional[EmailStr] = Query(
        None,
        title="Email of user",
        description="Email of The user",
        example="dd@testemail.com",
    ),
    mobileNumber: Optional[str] = Query(
        None,
        title="Mobile number of user",
        description="Mobile of The user",
        example="+91-9028077584",
    ),
):
    try:
        response_usr = delete_users(
            u_id=u_id, username=userName, email=emailAddress, mobile=mobileNumber
        )
        return {"status_delete": response_usr}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@access_manager_app.post(
    "/token",
    response_model=Token,
    tags=["Token Manager"],
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user_state, user = authenticate_user(
            user_name=form_data.username,
            password=form_data.password,
        )
        if user_state:
            userinfo = User(**user[0])
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"userName": userinfo.userName, "userType": userinfo.userType},
                expires_delta=access_token_expires,
            )
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
