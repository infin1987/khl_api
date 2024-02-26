from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from apiKhl.auth.dependencies import form_dep, db_dep
from apiKhl.auth.schemas import UserInDB, User, UserBase, Token
from apiKhl.auth.service import get_current_active_user, login_user


auth_router = APIRouter()


@auth_router.post('/token')
async def login(
        form_data: form_dep,
        db: db_dep
) -> Token:

    return await login_user(form_data, db)


@auth_router.post('/refresh_token')
async def refresh_token(token: Token,
                        db: db_dep):

    return {'message': 'This func is going to be launched soon'}


@auth_router.get('/whoami', response_model=UserBase)
async def whoami(user: Annotated[User, Depends(get_current_active_user)]):
    return user
