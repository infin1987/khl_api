from clickhouse_sqlalchemy import make_session
from sqlalchemy.orm import Session

from settings import settings

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine_data = create_async_engine(settings.DB_DATA_URL, future=True, echo=True)
async_session_data = async_sessionmaker(engine_data, expire_on_commit=False)
# async_session_data = make_session(engine_data, is_async=True)

async def get_db_data() -> AsyncSession:
# async def get_db_data() -> Session:
    try:
        session: AsyncSession | Session = async_session_data()
        # session: AsyncSession | Session = make_session(engine_data, is_async=True)
        # session: Session = async_session_data()
        print('giving data_connection')
        yield session
    finally:
        print('closing conn to dataDB')
        # await session.close()
        await session.aclose()
        # pass
