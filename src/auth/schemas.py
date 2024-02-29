from datetime import datetime
from enum import Enum, StrEnum
from typing import Annotated

from pydantic import BaseModel


class UserRoles(str, Enum):
    ADMIN = "admin"
    USER = "user"
    STAFF = "staff"
    CIB = 'cib'
    MOB_APP = 'mobile_app'
    MTV = 'match_tv'


class TokenSecretKey(StrEnum):
    REFRESH_TOKEN_SECRET_KEY = 'refresh'
    ACCESS_TOKEN_SECRET_KEY = 'access'


class TokenExpires(StrEnum):
    REFRESH_TOKEN_EXPIRES_MINUTES = 'refresh'
    ACCESS_TOKEN_EXPIRES_MINUTES = 'access'


class UserBase(BaseModel):
    username: str
    email: str | None = None
    role: UserRoles | None = UserRoles.USER


class UserCreate(UserBase):
    password: str
    active: bool = True


class User(UserBase):
    # id: int
    active: bool


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    action: str = 'created'


class TokenData(BaseModel):
    username: str | None = None
    role: UserRoles | None = UserRoles.USER
    expire: datetime


class TokenRefreshData(BaseModel):
    refresh_token: str
