from datetime import datetime
import logging
from app.database import Manager, Batch, Connection
from ..utils import calculateAge

logger = logging.getLogger(__name__)

batch = Manager(model=Batch)


def create_batch(batch_dict: dict) -> dict:
    """Create batch in database

    Args:
        batch_dict (dict): batch information in dictionary

    Returns:
        dict: Dict of Created batch
    """
    try:
        batch_dict["updatedAt"] = datetime.utcnow()
        batch_dict["age"] = calculateAge(batch_dict["birthDate"])
        with Connection():
            filter_batch = {}
            filter_batch.update({"instituteId": batch_dict["instituteId"]})
            batch_dict["u_id"] = batch.generate_id(filter_batch)
            batch_obj = batch.create(data_dict=batch_dict)
        return batch_obj
    except Exception as e:
        logger.exception("Exception occured while storing batch {}".format(e))
        raise Exception(str(e))


def update_batch(batch_id: int, update_dict: dict) -> dict:
    """Update batch in database

    Args:
        batch_id (int): batch id
        update_dict (dict): batch information in dictionary

    Returns:
        dict: Dict of Created batches
    """
    try:
        update_dict["updatedAt"] = datetime.utcnow()
        if "birthDate" in update_dict:
            update_dict["age"] = calculateAge(update_dict["birthDate"])
        with Connection():
            batch_obj = batch.update(data_id=batch_id, update_dict=update_dict)
        return batch_obj
    except Exception as e:
        logger.exception("Exception occured while updating Batch {}".format(e))
        raise Exception(str(e))


def get_batch(
    institute_id: int = None,
    batch_id: int = None,
    batch_name: str = None,
) -> list:
    """Get Batch

    Args:
        institute_id (int, optional): institute id. Defaults to None.
        batch_id (int, optional): Batch id. Defaults to None.
        batch_name (str, optional): Batch name. Defaults to None.

    Raises:
        Exception: Batch filter exception

    Returns:
        list: List of Batches
    """
    try:
        filter_batch = {}
        if institute_id:
            filter_batch.update({"instituteId": institute_id})
        if batch_id:
            filter_batch.update({"u_id": batch_id})
        if batch_name:
            filter_batch.update({"batchName": batch_name})
        with Connection():
            batch_obj = batch.read(filter_dict=filter_batch)
        return batch_obj
    except Exception as e:
        logger.exception("Exception occured while getting batches {}".format(e))
        raise Exception(str(e))


def delete_batch(
    institute_id: int = None,
    batch_id: int = None,
    batch_name: str = None,
) -> bool:
    """Delete Batches

    Args:
        institute_id (int, optional): institute id. Defaults to None.
        batch_id (int, optional): Batch id. Defaults to None.
        batch_name (str, optional): Batch name. Defaults to None.

    Raises:
        Exception: Batch filter exception

    Returns:
        bool: State of deletion
    """
    try:
        filter_batch = {}
        if institute_id:
            filter_batch.update({"instituteId": institute_id})
        if batch_id:
            filter_batch.update({"u_id": batch_id})
        if batch_name:
            filter_batch.update({"batchName": batch_name})
        with Connection():
            batch_state = batch.delete(data_filter=filter_batch)
        return batch_state
    except Exception as e:
        logger.exception("Exception occured while deleting batch {}".format(e))
        raise Exception(str(e))
