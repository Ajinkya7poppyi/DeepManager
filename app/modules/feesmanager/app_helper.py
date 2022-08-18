from datetime import datetime
import logging
from typing import List
from app.database import Manager, Fees, Connection
from .models import Fees, UserType

logger = logging.getLogger(__name__)

fees = Manager(model=Fees)


def create_fees(fees_dict: dict) -> dict:
    """Create fees in database

    Args:
        fees_dict (dict): fees information in dictionary

    Returns:
        dict: Dict of Created fees
    """
    try:
        fees_dict["updatedAt"] = datetime.utcnow()
        with Connection():
            filter_usr = {}
            filter_usr.update({"instituteId": fees_dict["instituteId"]})
            fees_dict["u_id"] = fees.generate_id(data_filter=filter_usr)
            f = fees.create(data_dict=fees_dict)
        return f
    except Exception as e:
        logger.exception("Exception occured while storing fees {}".format(e))
        raise Exception(str(e))


def update_fees(fees_id: int, fees_dict: dict) -> dict:
    """Update fees in database

    Args:
        fees_dict (dict): Fees information in dictionary

    Returns:
        dict: Dict of Created Fees
    """
    try:
        fees_dict["updatedAt"] = datetime.utcnow()
        with Connection():
            f = fees.update(data_id=fees_id, update_dict=fees_dict)
        return f
    except Exception as e:
        logger.exception("Exception occured while updating fees {}".format(e))
        raise Exception(str(e))


def get_fees(
    u_id: int = None,
    userId: int = None,
    batchId: int = None,
    userType: UserType = None,
    transactionDate: List[datetime] = None,
) -> list:
    """Get Fees

    Args:
        u_id (int, optional): Transaction id. Defaults to None.
        userId (int, optional): User id. Defaults to None.
        userType (str, optional): User type. Defaults to None.
        batchId (int, optional): Batch id. Defaults to None.
        transactionDate (List[datetime], optional): Transaction Date range. Defaults to None.

    Raises:
        Exception: Fees filter exception

    Returns:
        list: List of transactions
    """
    try:
        filter_fees = {}
        if u_id:
            filter_fees.update({"u_id": u_id})
        if userId:
            filter_fees.update({"userId": userId})
        if userType:
            filter_fees.update({"userType": userType})
        if batchId:
            filter_fees.update({"batchId": batchId})
        f_list = list()
        with Connection():
            if transactionDate:
                for i in transactionDate:
                    filter_fees["createdAt"] = i
                    f_list.extend(fees.read(filter_dict=filter_fees))
            else:
                f_list = fees.read(filter_dict=filter_fees)
        return f_list
    except Exception as e:
        logger.exception("Exception occured while getting fees {}".format(e))
        raise Exception(str(e))


def delete_fees(
    u_id: int = None,
    userId: int = None,
    batchId: int = None,
    userType: UserType = None,
    transactionDate: List[datetime] = None,
) -> bool:
    """Get Fees

    Args:
        u_id (int, optional): Transaction id. Defaults to None.
        userId (int, optional): User id. Defaults to None.
        userType (str, optional): User type. Defaults to None.
        batchId (int, optional): Batch id. Defaults to None.
        transactionDate (List[datetime], optional): Transaction Date range. Defaults to None.

    Raises:
        Exception: Fees filter exception

    Returns:
        bool: State of deletion
    """
    try:
        filter_fees = {}
        if u_id:
            filter_fees.update({"u_id": u_id})
        if userId:
            filter_fees.update({"userId": userId})
        if userType:
            filter_fees.update({"userType": userType})
        if batchId:
            filter_fees.update({"batchId": batchId})
        with Connection():
            if transactionDate:
                for i in transactionDate:
                    filter_fees["createdAt"] = i
                    f_list = fees.delete(data_filter=filter_fees)
            else:
                f_list = fees.delete(data_filter=filter_fees)
        return f_list
    except Exception as e:
        logger.exception("Exception occured while deleting fees {}".format(e))
        raise Exception(str(e))
