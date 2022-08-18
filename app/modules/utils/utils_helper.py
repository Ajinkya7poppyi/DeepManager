from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Optional
from jose import jwt
from .config_loader import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def calculateAge(born):
    today = datetime.today().date()
    try:
        birthday = born.replace(year=today.year)

    # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year=today.year, month=born.month + 1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify Password

    Args:
        plain_password (str): Plain password
        hashed_password (str): Hashed password

    Returns:
        bool: User Password Verification
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> jwt:
    """Create Access Token

    Args:
        data (dict): Data for creating token
        expires_delta (Optional[timedelta], optional): Time of token expiry. Defaults to None.

    Returns:
        jwt: JWT token to user
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
