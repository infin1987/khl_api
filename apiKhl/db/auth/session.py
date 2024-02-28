from redis.asyncio.client import Redis

from apiKhl.settings import settings
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from .models import fake_db
import redis.asyncio as redis

# engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)

# async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_redis_client() -> Redis:
    try:
        print('trying to establish redis connection')
        client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )
        print(type(client))
        yield client
    finally:
        print('closing conn to redis')
        await client.aclose()

async def get_db() -> AsyncGenerator | dict:
    try:
        # session: AsyncSession = async_session()
        print('giving fakedb')
        yield fake_db
    finally:
        print('closing conn to fakedb')
        # await session.close()
        pass
