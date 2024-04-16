import pytest
from httpx import AsyncClient, ASGITransport

from src.main import app


@pytest.fixture(scope="session")
async def ac():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
