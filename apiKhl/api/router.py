from typing import Annotated

from fastapi import APIRouter, Depends
from apiKhl.auth.schemas import Token
from apiKhl.auth.service import oauth2_scheme
api_router = APIRouter()

@api_router.get('/')
async def secured_data(token: Annotated[str, Depends(oauth2_scheme)]):
    return {'token': token}