from datetime import timedelta, datetime
from typing import Annotated, Literal

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from apiKhl.auth.dependencies import db_dep
from apiKhl.auth.exceptions import noUserException
from apiKhl.auth.schemas import User, UserInDB, Token, TokenSecretKey, TokenExpires
from apiKhl.db.auth.session import get_db
from apiKhl.settings import settings
from passlib.context import CryptContext
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: db_dep
) -> User:
    print(token)
    token_data = jwt.decode(token, settings.ACCESS_TOKEN_SECRET_KEY, algorithms=[settings.ALGORITHM])
    print(token_data)
    user_dict = db.get(token_data.get('user'))
    if not user_dict:
        print('user not in dict')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate credentials",
                            headers={"WWW-Authenticate": "Bearer"}
                            )
    return User(**user_dict)


async def get_current_active_user(
        current_user: User = Depends(get_current_user)
) -> User:
    if not current_user.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(db, username: str, password: str) -> UserInDB:
    """async because later it is going to contact with DB """
    user = db.get(username)
    if not user:
        raise noUserException
    user = UserInDB(**user)
    if not verify_password(password, user.hashed_password):
        raise noUserException
    return user


def create_token(data: dict,
                 expires_delta: timedelta | None = None,
                 token_kind: Literal['access', "refresh"] = 'access'
                 ) -> str:
    TOKEN_SECRET_KEY = getattr(settings, TokenSecretKey(token_kind).name)
    TOKEN_EXPIRES_MINUTE = getattr(settings, TokenExpires(token_kind).name)
    to_encode = data.copy()
    if expires_delta is not None:
        exp_date = datetime.now() + expires_delta
    else:
        exp_date = datetime.now() + timedelta(minutes=TOKEN_EXPIRES_MINUTE)
    to_encode.update({'exp': exp_date})
    encoded_jwt = jwt.encode(to_encode, TOKEN_SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def login_user(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: db_dep
) -> Token:
    user = await authenticate_user(db, form_data.username, form_data.password)
    access_token = create_token(data={'user': user.username}, token_kind='access')
    refresh_token = create_token(data={'sub': user.username}, token_kind='access')
    # TODO: issue access and refresh here
    return Token(access_token=access_token, token_type='bearer', refresh_token=refresh_token)
