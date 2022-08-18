import logging
from mongoengine.document import Document
from mongoengine.errors import NotUniqueError, OperationError, InvalidDocumentError
from ..utils.exceptions import CreateError

logger = logging.getLogger(__name__)


def add_object(model: Document, obj_info: dict) -> dict:
    """Add object information to mongodb

    Args:
        obj_info (dict): dictionary with informations about object

    Returns:
        dict: dictionary with information about object
    """
    try:
        data_obj = model(**obj_info).save()
        obj = data_obj.to_mongo().to_dict()
        return obj
    except NotUniqueError as e:
        logger.exception("Exception Occured while storing data {}".format(e))
        raise CreateError("Duplicate Details")
    except OperationError as e:
        logger.exception("Exception Occured while storing data {}".format(e))
        raise CreateError("Could not save data")
    except InvalidDocumentError as e:
        logger.exception("Exception Occured while storing data {}".format(e))
        raise CreateError("Invalid data Error")
    except Exception as e:
        logger.exception("Exception Occured while storing data {}".format(e))
        raise CreateError("Could not complete operation")
