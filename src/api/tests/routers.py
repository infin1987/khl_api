from fastapi import APIRouter
from uuid import uuid4

tests_router = APIRouter()


uuid = uuid4()


@tests_router.get("/")
async def root():
    return {'uuid': uuid}
