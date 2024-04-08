from typing import Annotated

from fastapi import APIRouter, Query, Path, Depends
from sqlalchemy import select, desc

from api.dependencies import db_dep
from api.players.schemas import PlayersTotalResponse
from db.api.models.player import PlayersBio, PlayersTotal
from db.api.models.tournaments import Tournaments
from service.helpers import check_last_updated
from service.players.handlers import get_player_stats_by_metric

from service.players.helpers import helper_dep

from error_handling_config import _info

players_router = APIRouter(prefix='/players', tags=['players'],
                           dependencies=[Depends(check_last_updated)])


@players_router.get('/stats')
async def get_players_filtered(q: str = None):
    return {'data': 'all players filtered data'}


@players_router.get('')
async def get_players_bio(
        db: db_dep,
):
    data = await db.execute(select(PlayersBio))
    _info(f"data: {data}")
    ret = data.scalars().all()
    _info(f"len(ret): {len(ret)}")
    return ret


@players_router.get('/total', response_model=list[PlayersTotalResponse])
async def get_players_total(
        db: db_dep,
        tnt_id: Annotated[str | None, Query()] = None,
):
    if not tnt_id:
        stmt = select(Tournaments.tnt_id).order_by(desc(Tournaments.tnt_id))
        tnt_id_data = await db.execute(stmt)
        tnt_id = tnt_id_data.scalars().first()

    data = await db.execute(select(PlayersTotal).where(PlayersTotal.tnt_id == tnt_id))
    ret = data.scalars().all()
    return ret


@players_router.get('/{player_id}/metrics/{metric}/')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def player_stats_by_metric(
        player_id: Annotated[int, Path()],
        db: db_dep,
        helper_obj: helper_dep,
):
    # TODO: прикрутить авторизацию - выше закоменчена
    return await get_player_stats_by_metric(player_id=player_id, helper_obj=helper_obj, db=db)
