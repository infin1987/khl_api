import pytest
from httpx import AsyncClient, ASGITransport

from main import app

@pytest.mark.anyio
async def test_arenas_tnt():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/v1/arenas/34", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    # assert response.json() == {"message": "Tomato"}