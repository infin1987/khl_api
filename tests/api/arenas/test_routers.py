import pytest


# pytestmark = pytest.mark.asyncio(scope='session')


@pytest.mark.asyncio(scope="session")
async def test_arenas_tnt(fixture_client):
    idarena = 28
    response = await fixture_client.get(f"/api/v1/arenas/{idarena}", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    assert response.json()[0].get('idarena') == idarena
    assert response.json()[0].get('tnt_id') is not None
    assert response.json()[0].get('schedule_id') is None


@pytest.mark.asyncio(scope="session")
async def test_arenas_games(fixture_client):
    idarena = 28
    response = await fixture_client.get(f"/api/v1/arenas/{idarena}/games", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    assert response.json()[0].get('idarena') == idarena
    assert response.json()[0].get('tnt_id') is not None
    assert response.json()[0].get('schedule_id') is not None
    assert response.json()[0].get('teamname_a') is not None


@pytest.mark.asyncio(scope="session")
async def test_headers_absense_games(fixture_client):
    idarena = 28
    response = await fixture_client.get(f"/api/v1/arenas/{idarena}/games")
    assert response.status_code == 422


@pytest.mark.asyncio(scope="session")
async def test_headers_absense_tnt(fixture_client):
    idarena = 28
    response = await fixture_client.get(f"/api/v1/arenas/{idarena}")
    assert response.status_code == 422
