from datetime import datetime
import logging
from mongoengine.document import Document
from mongoengine.errors import (
    NotUniqueError,
    OperationError,
    InvalidDocumentError,
    DoesNotExist,
)
from ..utils.exceptions.crud import UpdateError

logger = logging.getLogger(__name__)


def update_objects(model: Document, id: int, update_dict: dict) -> dict:
    """Update object in MongoDB

    Args:
        id (str): id of object
        update_dict (dict): Dictionary of values to update

    Returns:
        dict: Updated dictionary
    """
    try:
        data_obj = model.objects(u_id=id)
        updatekwargs = dict()
        obj = {}
        if data_obj:
            for key, value in update_dict.items():
                if value is not None:
                    key = "set__" + key
                    updatekwargs[key] = value
            updatekwargs["updatedAt"] = datetime.utcnow()
            obj = (
                data_obj.modify(upsert=True, new=True, **updatekwargs)
                .to_mongo()
                .to_dict()
            )
        return obj
    except DoesNotExist as e:
        logger.exception("Exception Occured while storing data {}".format(e))
        raise UpdateError("User Does Not Exists Error")
    except OperationError as e:
        logger.exception("Exception Occured while storing data {}".format(e))
        raise UpdateError("Could not save data")
    except InvalidDocumentError as e:
        logger.exception("Exception Occured while storing data {}".format(e))
        raise UpdateError("Invalid data Error")
    except Exception as e:
        logger.exception("Exception Occured while storing data {}".format(e))
        raise UpdateError("Could not complete operation")
