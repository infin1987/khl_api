import pytest


@pytest.mark.asyncio
async def test_get_specific_operations(ac):
    response = await ac.get("/api/v1/players/stats",
                            headers={'Last-updated': '20213111'})

    assert response.status_code == 200
