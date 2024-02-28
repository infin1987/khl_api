from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from apiKhl.db.auth.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

db_dep = Annotated[AsyncSession | dict, Depends(get_db)]
form_dep = Annotated[OAuth2PasswordRequestForm, Depends()]
oauth2_dep = Annotated[str, Depends(oauth2_scheme)]