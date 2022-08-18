import logging
from mongoengine.document import Document
from mongoengine.queryset import Q
from mongoengine.errors import DoesNotExist, OperationError, InvalidQueryError
from ..utils.exceptions.crud import DeleteError

logger = logging.getLogger(__name__)


def remove_object(model: Document, obj_filter: dict) -> bool:
    """Remove object from MongoDB

    Args:
        obj_filter (dict): Filter for object

    Returns:
        bool: return true if deleted succesfully
    """
    try:
        obj_state = False
        query = Q()
        if obj_filter is not None:
            for i in range(len(obj_filter)):
                query = query & Q(**dict(list(obj_filter.items())[i : i + 1]))
        # data_obj = model.objects.get(**obj_filter)
        # if data_obj:
        #     obj_state = True
        #     data_obj.delete()
        data_objects = model.objects.filter(query)
        for u in data_objects:
            u.delete()
            obj_state = True
        return obj_state
    except DoesNotExist as e:
        logger.exception("Exception Occured while reading data {}".format(e))
        raise DeleteError("Object does not exist")
    except InvalidQueryError as e:
        logger.exception("Exception Occured while reading data {}".format(e))
        raise DeleteError("Invalid filter query")
    except OperationError as e:
        logger.exception("Exception Occured while reading data {}".format(e))
        raise DeleteError("Could not save data")
    except Exception as e:
        logger.exception("Exception Occured while reading data {}".format(e))
        raise DeleteError("Could not complete operation")
