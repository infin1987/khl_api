import pytest


@pytest.mark.asyncio
async def test_get_specific_operations(fixture_client):
    response = await fixture_client.get("/api/v1/players/stats",
                                        headers={'Last-updated': '20213111'})

    assert response.status_code == 200
