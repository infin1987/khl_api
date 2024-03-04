import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request, Path
from sqlalchemy import select, text, case
from sqlalchemy.orm import load_only, defer

from api.dependencies import db_dep
from auth.dependencies import oauth2_dep
from auth.schemas import Token
from auth.service import oauth2_scheme
from db.api.models import PlayerGoals, Base

api_router = APIRouter()


@api_router.get('/players/{player_id}/metrics/{metric}/')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def secured_data(
        player_id: Annotated[int, Path()],
        metric: Annotated[str, Path()],
        db: db_dep,
        last_updated: Annotated[int, Header()]):
    print(last_updated)
    tablename = f'pl_{metric}_api'
    # pl_goals_data = await db.execute(select(PlayerGoals.P, PlayerGoals.G_GP, PlayerGoals.global_id, PlayerGoals.P))
    # pl_goals_data = await db.execute(select(PlayerGoals)
    #                                  .where(case(
    #     (PlayerGoals.G_GP == 'NaN', 0),
    #     else_=PlayerGoals.G_GP
    # )))
    # stmt = select(PlayerGoals).where(case(
    #     (PlayerGoals.G_GP == 'NaN', 0),
    #     else_=PlayerGoals.G_GP
    # ))

    def get_model_by_name(name: str):
        for elem in Base.registry.mappers:
            print(elem.entity.__tablename__)
            if elem.entity.__tablename__ == name:
                return elem.entity

    req_model = get_model_by_name(tablename)
    print(req_model)
    stmt = select(req_model).options(defer(req_model.G_GP))
    data = await db.execute(stmt)
    # print(data.scalars().all())
    ret = [val.__dict__ for val in data.scalars().all()]
    # print(ret)
    # print(type(ret))
    # print(ret[0].__dict__)

    return ret

