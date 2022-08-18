from typing import List
from jose import JWTError, jwt, ExpiredSignatureError
import logging
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.database import Manager, User, Connection
from .models import TokenData
from ..utils import (
    get_password_hash,
    verify_password,
    SECRET_KEY,
    ALGORITHM,
)

logger = logging.getLogger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user = Manager(model=User)


def create_users(user_dict: dict) -> dict:
    """Create users in database

    Args:
        user_dict (dict): users information in dictionary

    Returns:
        dict: Dict of Created user
    """
    try:
        with Connection():
            u = user.create(data_dict=user_dict)
        return u
    except Exception as e:
        logger.exception("Exception occured while storing user {}".format(e))
        raise Exception(str(e))


def update_users(user_id: int, user_dict: dict) -> dict:
    """Update users in database

    Args:
        user_dict (dict): users information in dictionary

    Returns:
        dict: Dict of Created user
    """
    try:
        with Connection():
            u = user.update(data_id=user_id, update_dict=user_dict)
        return u
    except Exception as e:
        logger.exception("Exception occured while updating user {}".format(e))
        raise Exception(str(e))


def get_users(
    u_id: int = None, username: str = None, email: str = None, mobile: str = None
) -> list:
    """Get Users

    Args:
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
        if u_id:
            filter_usr.update({"u_id": u_id})
        if username:
            filter_usr.update({"userName": username})
        if email:
            filter_usr.update({"emailAddres": email})
        if mobile:
            filter_usr.update({"mobileNumber": mobile})
        with Connection():
            u = user.read(filter_dict=filter_usr)
        return u
    except Exception as e:
        logger.exception("Exception occured while getting user {}".format(e))
        raise Exception(str(e))


def delete_users(
    u_id: int = None, username: str = None, email: str = None, mobile: str = None
) -> bool:
    """Get Users

    Args:
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
        if u_id:
            filter_usr.update({"u_id": u_id})
        if username:
            filter_usr.update({"userName": username})
        if email:
            filter_usr.update({"emailAddres": email})
        if mobile:
            filter_usr.update({"mobileNumber": mobile})
        with Connection():
            u = user.delete(data_filter=filter_usr)
        return u
    except Exception as e:
        logger.exception("Exception occured while deleting user {}".format(e))
        raise Exception(str(e))


def authenticate_user(password: str, user_name: str) -> tuple:
    """Authenticate User

    Args:
        username (str): user name
        password (str): user password

    Returns:
        tuple: tupe of authentication state and User info
    """
    try:
        user = get_users(username=user_name)
        if not user:
            return False, None
        if not verify_password(password, get_password_hash(user[0]["userPassword"])):
            return False, None
        return True, user
    except Exception as e:
        logger.exception("Exception occured while authenticating user {}".format(e))
        raise Exception(str(e))


async def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
    """Get current user from token

    Args:
        token (str, optional): JWT token. Defaults to Depends(oauth2_scheme).

    Raises:
        credentials_exception: Incorrect credentials exception
        expired_exception: Token expired exception

    Returns:
        TokenData: Token data
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    expired_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token Expired",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("userName")
        userType: str = payload.get("userType")
        if username is None:
            raise credentials_exception
        token_data = TokenData(userName=username, userType=userType)
    except JWTError:
        raise credentials_exception
    except ExpiredSignatureError:
        raise expired_exception
    user = get_users(username=token_data.userName)
    if user is None:
        raise credentials_exception
    return TokenData(**user[0])
