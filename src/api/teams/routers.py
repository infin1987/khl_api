from typing import Annotated, Literal

from fastapi import APIRouter, Query, Request, Header, Path, Depends
from sqlalchemy import select, func, desc

from api.dependencies import db_dep
from api.players.schemas import PlayersGoalsQuery, PlayersTotalResponse
from db.api.models.teams import Teams_TM6
from db.api.models.tournaments import Tournaments
from exceptions import no_new_data_exception
from service.helpers import check_last_updated
from service.players.handlers import get_player_stats_by_metric

from service.players.helpers import helper_dep

teams_router = APIRouter(prefix='/teams', tags=['teams'], dependencies=[Depends(check_last_updated)])


@teams_router.get('/stats')
async def get_players_filtered(q: str = None):
    return {'data': 'all teams filtered data'}


@teams_router.get('')
async def get_players_bio(
        db: db_dep,
        tnt_id: Annotated[str | None, Query()] = None,
):
    data = await db.execute(select(Teams_TM6))
    ret = data.scalars().all()
    return ret


@teams_router.get('/{team_id}/metrics/{metric}/')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def player_stats_by_metric(
        player_id: Annotated[int, Path()],
        db: db_dep,
        helper_obj: helper_dep,
):
    return await get_player_stats_by_metric(player_id=player_id, helper_obj=helper_obj, db=db)


