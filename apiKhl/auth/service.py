import json
from datetime import timedelta, datetime, timezone
from typing import Annotated, Literal

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from apiKhl.auth.dependencies import db_dep, oauth2_dep, rcache_dep
from apiKhl.auth.exceptions import noUserException, credentialException, tokenExpiredException
from apiKhl.auth.repositories import get_user_repositories
from apiKhl.auth import schemas
from apiKhl.db.auth.session import get_db, get_redis_client
from apiKhl.settings import settings
from passlib.context import CryptContext
from jose import JWTError, jwt
from jose.exceptions import ExpiredSignatureError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# def validate_token(token: str, token_kind: schemas.TokenSecretKey) -> schemas.TokenData:
def validate_token(token: str, token_kind: schemas.TokenSecretKey) -> schemas.TokenData:
    """
    validates token and returns data contained in token
    :param token:
    :param token_kind:
    :return:
    """
    try:
        TOKEN_SECRET_KEY = getattr(settings, schemas.TokenSecretKey(token_kind).name)
        print(TOKEN_SECRET_KEY)
        token_data = jwt.decode(token, TOKEN_SECRET_KEY, algorithms=[settings.ALGORITHM])
        print(token_data)
        username: str = token_data.get('user')
        token_exp: int = token_data.get('exp')
        user_role: str = token_data.get('role')
        if not username:
            raise credentialException
        token_data = schemas.TokenData(username=username, expire=token_exp, role=user_role)
        print(token_data, token_exp - datetime.now(tz=timezone.utc).timestamp())
    except JWTError as e:
        if isinstance(e, ExpiredSignatureError):
            print(f'{token_kind.upper()} TOKEN EXPIRED!!!')
            raise tokenExpiredException
        print(e)
        raise credentialException
    return token_data


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: db_dep
) -> schemas.User:
    token_data = validate_token(token, token_kind=schemas.TokenSecretKey.ACCESS_TOKEN_SECRET_KEY)
    user_dict = await get_user_repositories(db=db, username=token_data.username)
    if not user_dict:
        raise credentialException
    return schemas.User(**user_dict)


async def get_current_active_user(
        current_user: Annotated[schemas.User, Depends(get_current_user)]
) -> schemas.User:
    if not current_user.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(db, username: str, password: str) -> schemas.UserInDB:
    """async because later it is going to contact with DB """
    user = db.get(username)
    print(user)
    if not user:
        raise noUserException
    user = schemas.UserInDB(**user)
    print(user)
    if not verify_password(password, user.hashed_password):
        raise noUserException
    return user


def create_token(data: dict,
                 expires_delta: timedelta | None = None,
                 token_kind: Literal['access', "refresh"] = 'access'
                 ) -> str:
    TOKEN_SECRET_KEY = getattr(settings, schemas.TokenSecretKey(token_kind).name)
    TOKEN_EXPIRES_MINUTE = getattr(settings, schemas.TokenExpires(token_kind).name)
    to_encode = data.copy()
    if expires_delta is not None:
        exp_date = datetime.now(timezone.utc) + expires_delta
    else:
        exp_date = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRES_MINUTE)
    print(f'EXP DATE OF TOKEN: {exp_date.timestamp()}, {datetime.now().timestamp()}')
    to_encode.update({'exp': exp_date})
    encoded_jwt = jwt.encode(to_encode, TOKEN_SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def login_user(
        form_data: OAuth2PasswordRequestForm,
        db: db_dep
) -> schemas.Token:
    user = await authenticate_user(db, form_data.username, form_data.password)
    access_token = create_token(data={'user': user.username, 'role': user.role}, token_kind='access')
    refresh_token = create_token(data={'user': user.username}, token_kind='refresh')
    return schemas.Token(access_token=access_token, token_type='bearer', refresh_token=refresh_token)

# async def validate_refresh_blacklist(
#         refresh_token: str,
#         rclient: Redis
# ):
#     is_blacklisted = await rclient.get(refresh_token.refresh_token)
#     if is_blacklisted:
#         raise tokenExpiredException
#     return rclient

#TODO: delete all dep from here and insert just properly mapped classes
async def refreshTokens(
        access_token: str,
        refresh_token: str,
        db: db_dep,
        rcache: rcache_dep
) -> schemas.Token:
    token_data = validate_token(refresh_token, token_kind='refresh')
    user_dict = await get_user_repositories(db=db, username=token_data.username)
    if not user_dict:
        raise credentialException

    is_blacklisted = await rcache.get(refresh_token)
    if is_blacklisted:
        print('Refresh token is blacklisted')
        raise tokenExpiredException
    await rcache.set(refresh_token, 1, ex=settings.REFRESH_TOKEN_EXPIRES_MINUTES)
    # TODO: add parent refresh_token as a value (to be able to kill all parents` tokens in case of vulnerability)

    access_token = create_token(data={'user': token_data.username, 'role': token_data.role}, token_kind='access')
    refresh_token = create_token(data={'user': token_data.username}, token_kind='refresh')
    return schemas.Token(access_token=access_token, token_type='bearer', refresh_token=refresh_token, action='updated')
