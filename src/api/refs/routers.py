from typing import Annotated

from fastapi import APIRouter, Depends, Path

from api.dependencies import db_dep
from service.refs.handlers import get_refs_stats_by_metric
from service.refs.helpers import helper_dep, helper_nometric_dep
from service.helpers import check_last_updated

refs_router = APIRouter(prefix='/refs',
                          tags=['refs'],
                          dependencies=[Depends(check_last_updated)])


@refs_router.get('/{idref}')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def arena_stats(
        idref: Annotated[int, Path()],
        db: db_dep,
        helper_obj: helper_nometric_dep,
):
    # TODO: прикрутить авторизацию - выше закоменчена
    return await get_refs_stats_by_metric(ref_id=idref, helper_obj=helper_obj, db=db)


@refs_router.get('/{idref}/games')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def arena_stats_by_metric(
        idref: Annotated[int, Path()],
        db: db_dep,
        helper_obj: helper_dep,
):
    # TODO: прикрутить авторизацию - выше закоменчена
    return await get_refs_stats_by_metric(ref_id=idref, helper_obj=helper_obj, db=db)
