from datetime import datetime
import logging
from app.database import Manager, Student, Connection
from ..utils import calculateAge

logger = logging.getLogger(__name__)

student = Manager(model=Student)


def create_student(user_dict: dict) -> dict:
    """Create student in database

    Args:
        user_dict (dict): users information in dictionary

    Returns:
        dict: Dict of Created user
    """
    try:
        user_dict["updatedAt"] = datetime.utcnow()
        user_dict["age"] = calculateAge(born=user_dict["birthDate"])
        with Connection():
            filter_usr = {}
            filter_usr.update({"instituteId": user_dict["instituteId"]})
            user_dict["u_id"] = student.generate_id(filter_usr)
            std = student.create(data_dict=user_dict)
        return std
    except Exception as e:
        logger.exception("Exception occured while storing Student {}".format(e))
        raise Exception(str(e))


def update_student(user_id: int, user_dict: dict) -> dict:
    """Update Student in database

    Args:
        user_dict (dict): users information in dictionary

    Returns:
        dict: Dict of Created Student
    """
    try:
        user_dict["updatedAt"] = datetime.utcnow()
        if "birthDate" in user_dict:
            user_dict["age"] = calculateAge(user_dict["birthDate"])
        with Connection():
            std = student.update(data_id=user_id, update_dict=user_dict)
        return std
    except Exception as e:
        logger.exception("Exception occured while updating Student {}".format(e))
        raise Exception(str(e))


def get_student(
    institute_id: int = None,
    u_id: int = None,
    username: str = None,
    email: str = None,
    mobile: str = None,
) -> list:
    """Get Students

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
            std = student.read(filter_dict=filter_usr)
        return std
    except Exception as e:
        logger.exception("Exception occured while getting student {}".format(e))
        raise Exception(str(e))


def delete_student(
    institute_id: int = None,
    u_id: int = None,
    username: str = None,
    email: str = None,
    mobile: str = None,
) -> bool:
    """Get Student

    Args:
        institute_id (str, optional): institute id. Defaults to None.
        u_id (str, optional): User id. Defaults to None.
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
            std = student.delete(data_filter=filter_usr)
        return std
    except Exception as e:
        logger.exception("Exception occured while deleting user {}".format(e))
        raise Exception(str(e))
