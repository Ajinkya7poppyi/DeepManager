import logging
from mongoengine.document import Document
from mongoengine.queryset import Q
from mongoengine.errors import DoesNotExist, OperationError, InvalidQueryError
from ..utils.exceptions.crud import ReadError


logger = logging.getLogger(__name__)


def get_objects(model: Document, obj_filter: dict = None) -> list:
    """Get objects with filter from MongoDB

    Args:
        obj_filter (dict): filter for objects

    Returns:
        list: List of objects doctionary
    """
    try:
        query = Q()
        if obj_filter is not None:
            for i in range(len(obj_filter)):
                query = query & Q(**dict(list(obj_filter.items())[i : i + 1]))
        data_objects = model.objects.filter(query)
        obj = list()
        for u in data_objects:
            obj.append(u.to_mongo().to_dict())
        return obj
    except DoesNotExist as e:
        logger.exception("Exception Occured while reading data {}".format(e))
        raise ReadError("User does not exist")
    except InvalidQueryError as e:
        logger.exception("Exception Occured while reading data {}".format(e))
        raise ReadError("Invalid filter query")
    except OperationError as e:
        logger.exception("Exception Occured while reading data {}".format(e))
        raise ReadError("Could not save data")
    except Exception as e:
        logger.exception("Exception Occured while reading data {}".format(e))
        raise ReadError("Could not complete operation")


def get_maxid(model: Document, obj_filter: dict = None) -> int:
    """Get Maximum id for object

    Args:
        obj_filter (dict, optional): filter for objects. Defaults to None.

    Raises:model
        ReadError: [description]

    Returns:
        int: Number of Objects
    """
    try:
        query = Q()
        if obj_filter is not None:
            for i in range(len(obj_filter)):
                query = query & Q(**dict(list(obj_filter.items())[i : i + 1]))
        max_count = model.objects.filter(query).count()
        return max_count
    except InvalidQueryError as e:
        logger.exception("Exception Occured while reading data {}".format(e))
        raise ReadError("Invalid filter query")
    except Exception as e:
        logger.exception("Exception Occured while reading data {}".format(e))
        raise ReadError("Could not complete operation")
