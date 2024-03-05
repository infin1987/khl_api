from redis.asyncio.client import Redis

from settings import settings
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from .models import fake_db
import redis.asyncio as redis

engine_data = create_async_engine(settings.DB_DATA_URL, future=True, echo=True)

# async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
async_sessionmaker_user = async_sessionmaker(engine_data, expire_on_commit=False)


# async def get_redis_client() -> Redis:
#     try:
#         print('trying to establish redis connection')
#         client = redis.Redis(
#             host=settings.REDIS_HOST,
#             port=settings.REDIS_PORT,
#             db=settings.REDIS_DB,
#             decode_responses=True
#         )
#         print(type(client))
#         yield client
#     finally:
#         print('closing conn to redis')
#         await client.aclose()

async def get_redis_client() -> Redis:
    async with redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True) as client:
        yield client


async def get_user_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker_user() as session:
        # yield session
        yield fake_db
