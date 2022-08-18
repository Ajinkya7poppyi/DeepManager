from typing import Optional, List
from fastapi import Body, Depends, HTTPException, status, Query
from pydantic import EmailStr
from .app_helper import create_batch, delete_batch, get_batch, update_batch
from .models import (
    Batch,
    BatchUpdate,
    BatchDelete,
    BatchReturn,
    Message,
    TokenData,
)
from fastapi import APIRouter
from ..accessmanager.app_helper import get_current_user

batch_manager_app = APIRouter(tags=["Batch Manager"])


@batch_manager_app.post(
    "/batch",
    summary="Create a new Batch",
    description="Add a new Batch",
    response_model=BatchReturn,
    response_description="Creates Batch",
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": Message}},
    tags=["Batch Manager"],
)
async def create_user(batch: Batch = Body(...)):
    try:
        response_batch = create_batch(batch_dict=batch.dict())
        if response_batch:
            return response_batch
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@batch_manager_app.get(
    "/batch",
    summary="Get all Batches",
    description="Get all Batches",
    response_model=List[BatchReturn],
    response_description="Get all Batches",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Batch Manager"],
)
async def get_user(
    current_user: TokenData = Depends(get_current_user),
    instituteId: int = Query(
        None, title="Institute Id", description="Id of The Institute", example=123
    ),
    batch_id: Optional[int] = Query(
        None, title="Batch Id", description="Id of The Batch", example=12345
    ),
    batchName: Optional[str] = Query(
        None,
        title="Trainer Name",
        description="UserName of The Trainer",
        example="adam_sit",
    ),
):
    try:
        response_batch = get_batch(
            institute_id=instituteId,
            batch_id=batch_id,
            batch_name=batchName,
        )
        return response_batch
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@batch_manager_app.put(
    "/batch",
    summary="Update a Batch",
    description="Update a Batch",
    response_model=BatchReturn,
    status_code=status.HTTP_202_ACCEPTED,
    responses={400: {"model": Message}},
    tags=["Batch Manager"],
)
async def update_user(
    current_user: TokenData = Depends(get_current_user),
    batch_id: int = Query(
        ..., title="User Id", description="Id of The user", example=123
    ),
    batch: BatchUpdate = Body(...),
):
    try:
        response_batch = update_batch(batch_id=batch_id, update_dict=batch.dict())
        return response_batch
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@batch_manager_app.delete(
    "/batch",
    summary="Delete a Batch",
    description="Delete a Batch",
    response_description="Delete Batch",
    response_model=BatchDelete,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Batch Manager"],
)
async def delete_user(
    current_user: TokenData = Depends(get_current_user),
    instituteId: int = Query(
        None, title="Institute Id", description="Id of The Institute", example=123
    ),
    batch_id: Optional[int] = Query(
        None, title="Batch Id", description="Id of The Batch", example=12345
    ),
    batchName: Optional[str] = Query(
        None,
        title="Batch Name",
        description="Batchname",
        example="adam_sit",
    ),
):
    try:
        response_batch = delete_batch(
            institute_id=instituteId, batch_id=batch_id, batch_name=batchName
        )
        return {"status_delete": response_batch}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
