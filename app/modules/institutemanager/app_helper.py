from datetime import datetime
import logging
from app.database import Manager, Institute, Connection
from app.modules.institutemanager.models import institute
from ..utils import calculateAge

logger = logging.getLogger(__name__)

institute = Manager(model=Institute)


def create_institute(inst_dict: dict) -> dict:
    """Create institute in database

    Args:
        inst_dict (dict): institute information in dictionary

    Returns:
        dict: Dict of Created institute
    """
    try:
        filter_usr = {}
        with Connection():
            inst_dict["u_id"] = institute.generate_id(data_filter=filter_usr)
            inst_dict["updatedAt"] = datetime.utcnow()
            inst = institute.create(data_dict=inst_dict)
        return inst
    except Exception as e:
        logger.exception("Exception occured while storing institute {}".format(e))
        raise Exception(str(e))


def update_institute(inst_id: str, inst_dict: dict) -> dict:
    """Update institute in database

    Args:
        inst_dict (dict): institute information in dictionary

    Returns:
        dict: Dict of Created institute
    """
    try:
        inst_dict["updatedAt"] = datetime.utcnow()
        with Connection():
            inst = institute.update(data_id=inst_id, update_dict=inst_dict)
        return inst
    except Exception as e:
        logger.exception("Exception occured while updating institute {}".format(e))
        raise Exception(str(e))


def get_institute(
    u_id: int = None,
    username: str = None,
    email: str = None,
    mobile: str = None,
) -> list:
    """Get institute

    Args:
        u_id (str, optional): institute id. Defaults to None.
        username (str, optional): institute name. Defaults to None.
        email (str, optional): Email address. Defaults to None.
        mobile (str, optional): Mobile number. Defaults to None.

    Raises:
        Exception: institute filter exception

    Returns:
        list: List of institute
    """
    try:
        filter_inst = {}
        if u_id:
            filter_inst.update({"u_id": u_id})
        if username:
            filter_inst.update({"userName": username})
        if email:
            filter_inst.update({"emailAddres": email})
        if mobile:
            filter_inst.update({"mobileNumber": mobile})
        with Connection() as conn:
            inst = institute.read(filter_dict=filter_inst)
        return inst
    except Exception as e:
        logger.exception("Exception occured while getting institute {}".format(e))
        raise Exception(str(e))


def delete_institute(
    u_id: int = None,
    username: str = None,
    email: str = None,
    mobile: str = None,
) -> bool:
    """Get institute

    Args:
        u_id (str, optional): institute id. Defaults to None.
        username (str, optional): institute name. Defaults to None.
        email (str, optional): Email address. Defaults to None.
        mobile (str, optional): Mobile number. Defaults to None.

    Raises:
        Exception: User filter exception

    Returns:
        bool: State of deletion
    """
    try:
        filter_inst = {}
        if u_id:
            filter_inst.update({"u_id": u_id})
        if username:
            filter_inst.update({"userName": username})
        if email:
            filter_inst.update({"emailAddres": email})
        if mobile:
            filter_inst.update({"mobileNumber": mobile})
        with Connection():
            inst = institute.delete(data_filter=filter_inst)
        return inst
    except Exception as e:
        logger.exception("Exception occured while deleting institute {}".format(e))
        raise Exception(str(e))
