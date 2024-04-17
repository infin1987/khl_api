from typing import Annotated

from fastapi import APIRouter, Depends, Path

from api.dependencies import db_dep
from service.trainers.handlers import get_trainers_stats_by_metric
from service.trainers.helpers import helper_dep, helper_nometric_dep
from service.helpers import check_last_updated

trainers_router = APIRouter(prefix='/trainers',
                        tags=['trainers'],
                        dependencies=[Depends(check_last_updated)])


@trainers_router.get('/{trainer_id}')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def trainers_stats(
        trainer_id: Annotated[int, Path()],
        db: db_dep,
        helper_obj: helper_nometric_dep,
):
    # TODO: прикрутить авторизацию - выше закоменчена
    return await get_trainers_stats_by_metric(trainer_id=trainer_id, helper_obj=helper_obj, db=db)


@trainers_router.get('/{trainer_id}/games')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def trainers_stats_by_metric(
        trainer_id: Annotated[int, Path()],
        db: db_dep,
        helper_obj: helper_dep,
):
    # TODO: прикрутить авторизацию - выше закоменчена
    return await get_trainers_stats_by_metric(trainer_id=trainer_id, helper_obj=helper_obj, db=db)
