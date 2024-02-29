from sqlalchemy.ext.asyncio import AsyncSession

from auth.schemas import User


async def get_user_repositories(db: dict | AsyncSession, username: str) -> User | str:
    return db.get(username)