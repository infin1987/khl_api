from typing import Annotated

from fastapi import APIRouter, Depends, Path

from api.dependencies import db_dep
from service.arenas.handlers import get_arenas_stats_by_metric
from service.arenas.helpers import helper_dep, helper_nometric_dep
from service.helpers import check_last_updated

arenas_router = APIRouter(prefix='/arenas',
                          tags=['arenas'],
                          dependencies=[Depends(check_last_updated)])


@arenas_router.get('/{idarena}')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def arena_stats(
        idarena: Annotated[int, Path()],
        db: db_dep,
        helper_obj: helper_nometric_dep,
):
    # TODO: прикрутить авторизацию - выше закоменчена
    return await get_arenas_stats_by_metric(arena_id=idarena, helper_obj=helper_obj, db=db)


@arenas_router.get('/{idarena}/games')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def arena_stats_by_metric(
        idarena: Annotated[int, Path()],
        db: db_dep,
        helper_obj: helper_dep,
):
    # TODO: прикрутить авторизацию - выше закоменчена
    return await get_arenas_stats_by_metric(arena_id=idarena, helper_obj=helper_obj, db=db)
