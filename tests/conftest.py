import pytest
from httpx import AsyncClient, ASGITransport

from main import app


# @pytest.fixture(scope="session")
# def anyio_backend() -> str:
#     return "asyncio"


@pytest.fixture(scope="session")
async def fixture_client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac