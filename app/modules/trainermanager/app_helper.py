from datetime import datetime
import logging
from app.database import Manager, Trainer, Connection
from ..utils import calculateAge

logger = logging.getLogger(__name__)

trainer = Manager(model=Trainer)


def create_trainer(user_dict: dict) -> dict:
    """Create trainer in database

    Args:
        user_dict (dict): users information in dictionary

    Returns:
        dict: Dict of Created user
    """
    try:
        user_dict["updatedAt"] = datetime.utcnow()
        user_dict["age"] = calculateAge(user_dict["birthDate"])
        with Connection():
            filter_usr = {}
            filter_usr.update({"instituteId": user_dict["instituteId"]})
            user_dict["u_id"] = trainer.generate_id(filter_usr)
            trnr = trainer.create(data_dict=user_dict)
        return trnr
    except Exception as e:
        logger.exception("Exception occured while storing Trainer {}".format(e))
        raise Exception(str(e))


def update_trainer(user_id: int, user_dict: dict) -> dict:
    """Update trainer in database

    Args:
        user_dict (dict): users information in dictionary

    Returns:
        dict: Dict of Created trainer
    """
    try:
        user_dict["updatedAt"] = datetime.utcnow()
        if "birthDate" in user_dict:
            user_dict["age"] = calculateAge(user_dict["birthDate"])
        with Connection():
            trnr = trainer.update(data_id=user_id, update_dict=user_dict)
        return trnr
    except Exception as e:
        logger.exception("Exception occured while updating Trainer {}".format(e))
        raise Exception(str(e))


def get_trainer(
    institute_id: int = None,
    u_id: int = None,
    username: str = None,
    email: str = None,
    mobile: str = None,
) -> list:
    """Get Trainer

    Args:
        institute_id (int, optional): institute id. Defaults to None.
        u_id (int, optional): User id. Defaults to None.
        username (str, optional): User name. Defaults to None.
        email (str, optional): Email address. Defaults to None.
        mobile (str, optional): Mobile number. Defaults to None.

    Raises:
        Exception: User filter exception

    Returns:
        list: List of users
    """
    try:
        filter_usr = {}
        if institute_id:
            filter_usr.update({"instituteId": institute_id})
        if u_id:
            filter_usr.update({"u_id": u_id})
        if username:
            filter_usr.update({"userName": username})
        if email:
            filter_usr.update({"emailAddres": email})
        if mobile:
            filter_usr.update({"mobileNumber": mobile})
        with Connection():
            trnr = trainer.read(filter_dict=filter_usr)
        return trnr
    except Exception as e:
        logger.exception("Exception occured while getting trainer {}".format(e))
        raise Exception(str(e))


def delete_trainer(
    institute_id: int = None,
    u_id: int = None,
    username: str = None,
    email: str = None,
    mobile: str = None,
) -> bool:
    """Get TRainer

    Args:
        institute_id (int, optional): institute id. Defaults to None.
        u_id (int, optional): User id. Defaults to None.
        username (str, optional): User name. Defaults to None.
        email (str, optional): Email address. Defaults to None.
        mobile (str, optional): Mobile number. Defaults to None.

    Raises:
        Exception: User filter exception

    Returns:
        bool: State of deletion
    """
    try:
        filter_usr = {}
        if institute_id:
            filter_usr.update({"instituteId": institute_id})
        if u_id:
            filter_usr.update({"u_id": u_id})
        if username:
            filter_usr.update({"userName": username})
        if email:
            filter_usr.update({"emailAddres": email})
        if mobile:
            filter_usr.update({"mobileNumber": mobile})
        with Connection():
            trnr = trainer.delete(data_filter=filter_usr)
        return trnr
    except Exception as e:
        logger.exception("Exception occured while deleting trainer {}".format(e))
        raise Exception(str(e))
