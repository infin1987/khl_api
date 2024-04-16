import pytest


# pytestmark = pytest.mark.asyncio(scope='session')


@pytest.mark.asyncio(scope="session")
async def test_refs_tnt(fixture_client):
    idref = 166
    response = await fixture_client.get(f"/api/v1/refs/{idref}", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    assert response.json()[0].get('idref') == idref
    assert response.json()[0].get('tnt_id') is not None
    assert response.json()[0].get('schedule_id') is None
    assert response.json()[0].get('f2') is not None


@pytest.mark.asyncio(scope="session")
async def test_refs_tnt_filter(fixture_client):
    idref = 166
    season = '2022-2023'
    response = await fixture_client.get(f"/api/v1/refs/{idref}?season=2022-2023", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    assert response.json()[0].get('idref') == idref
    assert response.json()[0].get('season') == season
    assert response.json()[0].get('tnt_id') is not None
    assert response.json()[0].get('schedule_id') is None
    assert response.json()[0].get('f2') is not None


@pytest.mark.asyncio(scope="session")
async def test_refs_games(fixture_client):
    idref = 166
    response = await fixture_client.get(f"/api/v1/refs/{idref}/games", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    assert response.json()[0].get('idref') == idref
    assert response.json()[0].get('tnt_id') is not None
    assert response.json()[0].get('schedule_id') is not None
    assert response.json()[0].get('f2') is not None


@pytest.mark.asyncio(scope="session")
async def test_refs_games_filter(fixture_client):
    idref = 166
    season = '2022-2023'
    response = await fixture_client.get(f"/api/v1/refs/{idref}/games?season=2022-2023", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    assert response.json()[0].get('idref') == idref
    assert response.json()[0].get('season') == season
    assert response.json()[0].get('tnt_id') is not None
    assert response.json()[0].get('schedule_id') is not None
    assert response.json()[0].get('f2') is not None


@pytest.mark.asyncio(scope="session")
async def test_headers_absense_games(fixture_client):
    idref = 166
    response = await fixture_client.get(f"/api/v1/refs/{idref}/games")
    assert response.status_code == 422


@pytest.mark.asyncio(scope="session")
async def test_headers_absense_tnt(fixture_client):
    idref = 166
    response = await fixture_client.get(f"/api/v1/refs/{idref}")
    assert response.status_code == 422
