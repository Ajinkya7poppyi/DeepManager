from pydantic import BaseModel, Field
from typing import Optional, List


class TokenData(BaseModel):
    """ Token Data """
    userName: Optional[str] = None
    userType: Optional[str] = None


class Token(BaseModel):
    """ JWT Token Model """
    access_token: str
    token_type: str
