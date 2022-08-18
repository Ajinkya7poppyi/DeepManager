from datetime import date, datetime
import logging
from app.database import Manager, Attendance, Connection

logger = logging.getLogger(__name__)

attendance = Manager(model=Attendance)


def create_attendance(attendance_dict: dict) -> dict:
    """Create attendance in database

    Args:
        attendance_dict (dict): attendance information in dictionary

    Returns:
        dict: Dict of Created attendance
    """
    try:
        filter_atten = {}
        filter_atten.update({"instituteId": attendance_dict["instituteId"]})
        attendance_dict["u_id"] = attendance.generate_id(filter_atten)
        attendance_dict["updatedAt"] = datetime.utcnow()
        with Connection():
            att_obj = attendance.create(data_dict=attendance_dict)
        return att_obj
    except Exception as e:
        logger.exception("Exception occured while storing attendance {}".format(e))
        raise Exception(str(e))


def update_attendance(attendance_id: str, update_dict: dict) -> dict:
    """Update attendance in database

    Args:
        attendance_id (str): attendance id
        update_dict (dict): attendance information in dictionary

    Returns:
        dict: Dict of Created attendance
    """
    try:
        update_dict["updatedAt"] = datetime.utcnow()
        with Connection():
            att_obj = attendance.update(data_id=attendance_id, update_dict=update_dict)
        return att_obj
    except Exception as e:
        logger.exception("Exception occured while updating attendance {}".format(e))
        raise Exception(str(e))


def get_attendance(
    institute_id: int = None,
    batch_id: int = None,
    attendance_date: date = None,
    user_type: str = None,
) -> list:
    """Get attendance

    Args:
        institute_id (int, optional): institute id. Defaults to None.
        batch_id (int, optional): Batch id. Defaults to None.
        attendance_date (date, optional): attendance date. Defaults to None.
        user_type (str, optional): user type. Defaults to None.


    Raises:
        Exception: Attendance filter exception

    Returns:
        list: List of Attences
    """
    try:
        filter_attendace = {}
        if institute_id:
            filter_attendace.update({"instituteId": institute_id})
        if batch_id:
            filter_attendace.update({"batchId": batch_id})
        if attendance_date:
            filter_attendace.update({"attendanceDate": attendance_date})
        if user_type:
            filter_attendace.update({"userType": user_type})
        with Connection():
            att_obj = attendance.read(filter_dict=filter_attendace)
        return att_obj
    except Exception as e:
        logger.exception("Exception occured while getting attendance {}".format(e))
        raise Exception(str(e))


def delete_attendace(
    institute_id: int = None,
    batch_id: int = None,
    attendance_date: date = None,
    user_type: str = None,
) -> bool:
    """Delete attendaces

    Args:
        institute_id (int, optional): institute id. Defaults to None.
        batch_id (int, optional): Batch id. Defaults to None.
        attendance_date (date, optional): attendance date. Defaults to None.
        user_type (str, optional): user type. Defaults to None.

    Raises:
        Exception: attendaces filter exception

    Returns:
        bool: State of attendaces
    """
    try:
        filter_attendace = {}
        if institute_id:
            filter_attendace.update({"instituteId": institute_id})
        if batch_id:
            filter_attendace.update({"batchId": batch_id})
        if attendance_date:
            filter_attendace.update({"attendanceDate": attendance_date})
        if user_type:
            filter_attendace.update({"userType": user_type})
        with Connection():
            att_state = attendance.delete(data_filter=filter_attendace)
        return att_state
    except Exception as e:
        logger.exception("Exception occured while deleting attendance {}".format(e))
        raise Exception(str(e))
