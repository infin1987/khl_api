from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.api.session import get_db_data

db_dep = Annotated[AsyncSession, Depends(get_db_data)]
last_update_dep = Annotated[bool, Depends()]