from httpx import AsyncClient
# from .conftest import client
import pytest


@pytest.mark.asyncio
async def test_get_specific_operations(ac: AsyncClient):
    response = await ac.get("/api/v1/players/stats")

    assert response.status_code == 200
#
#
# def test_get():
#     res = client.get("/api/v1/players/stats")
#     assert res.status_code == 200
