from typing import Annotated

from fastapi import APIRouter, Depends
from auth.schemas import Token
from auth.service import oauth2_scheme
api_router = APIRouter()

@api_router.get('/')
async def secured_data(token: Annotated[str, Depends(oauth2_scheme)]):
    return {'token': token}