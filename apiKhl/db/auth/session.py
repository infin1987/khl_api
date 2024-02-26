from apiKhl import settings
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from .models import fake_db

# engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)

# async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator | dict:
    try:
        # session: AsyncSession = async_session()
        yield fake_db
    finally:
        # await session.close()
        pass
