import pytest


# pytestmark = pytest.mark.asyncio(scope='session')


@pytest.mark.asyncio(scope="session")
async def test_trainers_tnt(fixture_client):
    trainer_id = 732
    response = await fixture_client.get(f"/api/v1/trainers/{trainer_id}", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    assert response.json()[0].get('trainer_id') == trainer_id
    assert response.json()[0].get('tnt_id') is not None
    assert response.json()[0].get('schedule_id') is None
    assert response.json()[0].get('f2') is not None


@pytest.mark.asyncio(scope="session")
async def test_trainers_tnt_filter(fixture_client):
    trainer_id = 732
    season = '2022-2023'
    response = await fixture_client.get(f"/api/v1/trainers/{trainer_id}?season=2022-2023", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    assert response.json()[0].get('trainer_id') == trainer_id
    assert response.json()[0].get('season') == season
    assert response.json()[0].get('tnt_id') is not None
    assert response.json()[0].get('schedule_id') is None
    assert response.json()[0].get('f2') is not None


@pytest.mark.asyncio(scope="session")
async def test_trainers_games(fixture_client):
    trainer_id = 732
    response = await fixture_client.get(f"/api/v1/trainers/{trainer_id}/games", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    assert response.json()[0].get('trainer_id') == trainer_id
    assert response.json()[0].get('tnt_id') is not None
    assert response.json()[0].get('schedule_id') is not None
    assert response.json()[0].get('f2') is not None


@pytest.mark.asyncio(scope="session")
async def test_trainers_games_filter(fixture_client):
    trainer_id = 732
    season = '2022-2023'
    response = await fixture_client.get(f"/api/v1/trainers/{trainer_id}/games?season=2022-2023", headers={'Last-updated': '20213111'})
    assert response.status_code == 200
    assert response.json()[0].get('trainer_id') == trainer_id
    assert response.json()[0].get('season') == season
    assert response.json()[0].get('tnt_id') is not None
    assert response.json()[0].get('schedule_id') is not None
    assert response.json()[0].get('f2') is not None


@pytest.mark.asyncio(scope="session")
async def test_headers_absense_games(fixture_client):
    trainer_id = 732
    response = await fixture_client.get(f"/api/v1/trainers/{trainer_id}/games")
    assert response.status_code == 422


@pytest.mark.asyncio(scope="session")
async def test_headers_absense_tnt(fixture_client):
    trainer_id = 732
    response = await fixture_client.get(f"/api/v1/trainers/{trainer_id}")
    assert response.status_code == 422
