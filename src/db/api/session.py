from typing import AsyncGenerator

from clickhouse_sqlalchemy import make_session
from sqlalchemy.orm import Session, DeclarativeBase

from settings import settings

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine_data = create_async_engine(settings.DB_DATA_URL, future=True, echo=True)
async_sessionmaker_data = async_sessionmaker(engine_data, expire_on_commit=False)

# async_session_data = make_session(engine_data, is_async=True)


async def get_db_data() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker_data() as session:
        yield session
