from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from redis.asyncio.client import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from db.auth.session import get_user_db, get_redis_client

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

db_dep = Annotated[AsyncSession | dict, Depends(get_user_db)]
form_dep = Annotated[OAuth2PasswordRequestForm, Depends()]
oauth2_dep = Annotated[str, Depends(oauth2_scheme)]
rcache_dep = Annotated[Redis, Depends(get_redis_client)]