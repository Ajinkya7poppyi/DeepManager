from datetime import date
from typing import Optional, List
from fastapi import Body, Depends, HTTPException, status, Query
from .app_helper import create_fees, get_fees, update_fees, delete_fees
from .models import (
    Fees,
    FeesReturn,
    FeesDelete,
    FeesUpdate,
    UserType,
    Message,
    TokenData,
)
from fastapi import APIRouter
from ..accessmanager.app_helper import get_current_user

fees_manager_app = APIRouter(tags=["Fees Manager"])


@fees_manager_app.post(
    "/fees",
    summary="Create a new fees transaction",
    description="Add a new Fee transcation",
    response_model=FeesReturn,
    response_description="Creates Fees Transaction",
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": Message}},
    tags=["Fees Manager"],
)
async def create_transaction(fee_transaction: Fees = Body(...)):
    try:
        response_fees = create_fees(fee_transaction.dict())
        if response_fees:
            return response_fees
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@fees_manager_app.get(
    "/fees",
    summary="Get all Fees",
    description="Get all Fees",
    response_model=List[FeesReturn],
    response_description="Get all Fees",
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Fees Manager"],
)
async def get_transactions(
    current_user: TokenData = Depends(get_current_user),
    u_id: Optional[int] = Query(
        None, title="Institute Id", description="Id of The Institute", example=123
    ),
    user_id: Optional[int] = Query(
        None, title="User Id", description="Id of The User", example=123
    ),
    batch_id: Optional[int] = Query(
        None, title="Batch Id", description="Id of The Batch", example=123
    ),
    user_type: Optional[UserType] = Query(
        None, title="User Type", description="Type of The User", example="student"
    ),
    transaction_date: Optional[List[date]] = Query(
        None,
        title="Transactional Date",
        description="Date of The Fees",
        example=["2020-01-01"],
    ),
):
    try:
        response_fees = get_fees(
            u_id=u_id,
            userId=user_id,
            batchId=batch_id,
            userType=user_type,
            transactionDate=transaction_date,
        )
        return response_fees
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@fees_manager_app.put(
    "/fees",
    summary="Update a Fees",
    description="Update a Fees",
    response_model=FeesReturn,
    status_code=status.HTTP_202_ACCEPTED,
    responses={400: {"model": Message}},
    tags=["Fees Manager"],
)
async def update_transaction(
    current_user: TokenData = Depends(get_current_user),
    u_id: int = Query(
        ..., title="u Id", description="Id of The Fees transaction", example=123
    ),
    fees_trans: FeesUpdate = Body(...),
):
    try:
        response_fees = update_fees(fees_id=u_id, fees_dict=fees_trans.dict())
        return response_fees
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@fees_manager_app.delete(
    "/fees",
    summary="Delete a Fees",
    description="Delete a Fees",
    response_description="Delete Fees",
    response_model=FeesDelete,
    status_code=status.HTTP_200_OK,
    responses={400: {"model": Message}},
    tags=["Fees Manager"],
)
async def delete_transaction(
    current_user: TokenData = Depends(get_current_user),
    u_id: Optional[int] = Query(
        None, title="Institute Id", description="Id of The Institute", example=123
    ),
    user_id: Optional[int] = Query(
        None, title="User Id", description="Id of The User", example=123
    ),
    batch_id: Optional[int] = Query(
        None, title="Batch Id", description="Id of The Batch", example=123
    ),
    user_type: Optional[UserType] = Query(
        None, title="User Type", description="Type of The User", example="student"
    ),
    transaction_date: Optional[List[date]] = Query(
        None,
        title="Transactional Date",
        description="Date of The Fees",
        example=["2020-01-01"],
    ),
):
    try:
        response_fees = delete_fees(
            u_id=u_id,
            batchId=batch_id,
            userId=user_id,
            userType=user_type,
            transactionDate=transaction_date,
        )
        return {"status_delete": response_fees}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
