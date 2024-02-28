from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from apiKhl.auth.dependencies import form_dep, db_dep, oauth2_dep
from apiKhl.auth.schemas import UserInDB, User, UserBase, Token, TokenRefreshData
from apiKhl.auth.service import get_current_active_user, login_user, refreshTokens


auth_router = APIRouter()


@auth_router.post('/token')
async def login(
        form_data: form_dep,
        db: db_dep
) -> Token:

    return await login_user(form_data, db)


@auth_router.post('/refresh_token')
async def refreshToken(
        refresh_token: TokenRefreshData,
        access_token: oauth2_dep,
        db: db_dep
):
    print(f'{access_token=}')
    return await refreshTokens(access_token=access_token, refresh_token=refresh_token.refresh_token, db=db)


@auth_router.get('/whoami', response_model=UserBase)
async def whoami(user: Annotated[User, Depends(get_current_active_user)]):
    return user
