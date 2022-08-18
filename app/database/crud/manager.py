import uuid
import logging
from mongoengine import connect
from mongoengine.document import Document
from .create import add_object
from .delete import remove_object
from .update import update_objects
from .read import get_objects, get_maxid


logger = logging.getLogger(__name__)


class Manager:
    """Manager"""

    def __init__(self, model: Document):
        """Initialize Database Model

        Raises:
            Exception: Connection failure
        """
        try:
            self.model = model
        except Exception as e:
            logger.exception(
                "Exception Occured while getting databse model {}".format(e)
            )
            raise Exception("Model Creation Failure")

    def create(self, data_dict: dict) -> dict:
        """Create Object

        Args:
            data_dict (dict): Object dict

        Returns:
            dict: Object dict

        Raises:
            Exception: Object Creation Failure
        """
        try:
            obj = add_object(model=self.model, obj_info=data_dict)
            return obj
        except Exception as e:
            logger.exception("Exception Occured while storing object {}".format(e))
            raise Exception(str(e))

    def read(self, filter_dict: dict = None) -> dict:
        """Read Object

        Args:
            filter_dict (dict, optional): dict to filter Object. Defaults to None.

        Returns:
            dict: Object dict

        Raises:
            Exception: Failure in accessing objects
        """
        try:
            obj_list = get_objects(model=self.model, obj_filter=filter_dict)
            return obj_list
        except Exception as e:
            logger.exception("Exception Occured while reading objects {}".format(e))
            raise Exception(str(e))

    def update(self, data_id: int, update_dict: str) -> dict:
        """Update Object

        Args:
            data_id (int): object_id
            update_dict (dict): dict information update for Object

        Returns:
            dict: Object Json

        Raises:
            Exception: Object Updating Failure
        """
        try:
            obj = update_objects(model=self.model, id=data_id, update_dict=update_dict)
            return obj
        except Exception as e:
            logger.exception("Exception Occured while updating Object {}".format(e))
            raise Exception(str(e))

    def delete(self, data_filter: dict = None) -> bool:
        """Delete Object

        Args:
            data_filter (dict, optional): Object Filter. Defaults to None.

        Returns:
            bool: Object bool

        Raises:
            Exception: Batch Deleting Failure
        """
        try:
            obj = remove_object(model=self.model, obj_filter=data_filter)
            return obj
        except Exception as e:
            logger.exception("Exception Occured while deleting Object {}".format(e))
            raise Exception(str(e))

    def generate_id(self, data_filter: dict = None) -> int:
        """Get Max Id

        Args:
            data_filter (dict, optional): Object Filter. Defaults to None.

        Returns:
            int: Object id

        Raises: Object Max-fetching Failure
        """
        try:
            id_max = get_maxid(model=self.model, obj_filter=data_filter)
            return id_max
        except Exception as e:
            logger.exception("Exception Occured while getting max id {}".format(e))
            raise Exception(str(e))
