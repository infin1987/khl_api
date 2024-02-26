from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from apiKhl.db.auth.session import get_db

db_dep = Annotated[AsyncSession | dict, Depends(get_db)]
form_dep = Annotated[OAuth2PasswordRequestForm, Depends()]