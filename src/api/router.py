import datetime
from typing import Annotated
import api.schemas as api_schemas

from fastapi import APIRouter, Depends, Header, Request, Path
from sqlalchemy import select, text, case, and_, or_, desc, func
from sqlalchemy.orm import load_only, defer, InstrumentedAttribute

from api.dependencies import db_dep
from auth.dependencies import oauth2_dep
from auth.schemas import Token
from auth.service import oauth2_scheme
from db.api.models.player import PlayerGoals, PlayerGoalsFilter, PlayerMetricMixin, PlayerMetricFilteredMixin, \
    PlayerPenalties
from db.api.config import Base
from api.schemas import PlayerGoalsQuery, PlayerGoalsFilteredQuery

api_router = APIRouter()


def get_model_by_metric(metric: str):
    for elem in Base.registry.mappers:
        # print({el: vl for el, vl in elem.entity.__dict__.items() if isinstance(vl, InstrumentedAttribute)})
        print(elem.entity.__table__.columns)
        if elem.entity.__tablename__ == metric:
            return elem.entity


def get_schema_by_metric(metric: str):
    return getattr(api_schemas, f'Player{metric.capitalize()}FilteredQuery')


def get_proper_orm_model(
        metric: Annotated[str, Path()],
        league: str | None = None,
        tnt_id: int | None = None,
        tnt_type: str | None = None,
        time_period: int | None = None,
        team_status: str | None = None,
        net: str | None = None,
        position: str | None = None,
) -> PlayerGoals | PlayerGoalsFilter:
    params = league, tnt_id, tnt_type, time_period, team_status, net, position
    tablename = f'pl_{metric}_api_filters' if any(params) else f'pl_{metric}_api'
    return get_model_by_metric(tablename)


@api_router.get('/players/{player_id}/metrics/{metric}/all')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def secured_data(
        player_id: Annotated[int, Path()],
        # metric: Annotated[str, Path()],
        # query: Annotated[list, Depends()],
        req_model: Annotated[PlayerGoals | PlayerGoalsFilter, Depends(get_proper_orm_model)],
        db: db_dep,
        last_updated: Annotated[int, Header()],
        request: Request
):
    stmt = select(req_model).where(req_model.global_id == player_id).order_by(desc(req_model.tnt_id))
    data = await db.execute(stmt)
    ret = [val.__dict__ for val in data.scalars().all()]
    return ret


@api_router.get('/players/{player_id}/metrics/{metric}/')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def secured_data(
        player_id: Annotated[int, Path()],
        metric: Annotated[str, Path()],
        # query: Annotated[list, Depends()],
        req_model: Annotated[PlayerMetricFilteredMixin, Depends(get_proper_orm_model)],
        db: db_dep,
        last_updated: Annotated[int, Header()],
        request: Request
):
    print(last_updated, req_model)
    """Тут надо суммировать по всем полям показателей"""
    req_scheme = get_schema_by_metric(metric)
    colsNames = req_model.__table__.columns.keys()
    # print(cols)
    # print(req_model.get_columns())
    # vals = {el: vl for el, vl in req_model.__dict__.items() if isinstance(vl, InstrumentedAttribute)}
    # print(req_model.__class__.__dict__)
    # print(vars(req_model.__class__))

    vals = [vl for el, vl in req_model.__dict__.items() if isinstance(vl, InstrumentedAttribute)]

    colsToSum = {name:func.sum(col).label(name) for name, col in req_model.__table__.columns.items() if name in req_model.get_columns()}
    print(colsToSum)
    print(request.query_params)
    qp = req_scheme.model_validate(request.query_params).model_dump(by_alias=True)
    print(type(qp), qp)
    query_params = {k: v for k, v in req_scheme.model_validate(request.query_params) if v}
    print(query_params)
    ands = [getattr(req_model, param_name) == param_value for param_name, param_value in
            query_params.items() if param_value]
    group_bys = [getattr(req_model, param_name) for param_name, param_value in query_params.items()]
    # print(ands)
    # print(type(getattr(req_model, 'tnt_id')))
    # sts = req_model.tnt_id == 1078, req_model.tnt_type == 'r'
    # stmt = select(req_model).where(and_(*ands)).options(defer(req_model.G_GP))
    # stmt = select(req_model).where(and_(*ands))
    # stmt = select(req_model).filter_by(global_id=player_id).filter_by(**request.query_params)
    # stmt = select(req_model.time_period, *colsToSum).filter_by(global_id=player_id).group_by(
    #     req_model.time_period)
    # stmt = select(req_model.time_period, func.sum(req_model.G)).filter_by(global_id=player_id).group_by(
    #     req_model.time_period)
    # stmt = select(req_model).filter_by(**query_params)
    # stmt = select(req_model.time_period, func.sum(req_model.G)).filter_by(**query_params.model_dump(by_alias=True)).group_by(req_model.time_period)
    # print(query_params, *map(lambda x: print(x.name), colsToSum))
    # stmt = select(req_model.time_period, *colsToSum.values()).filter_by(global_id=player_id).group_by(*query_params.values())
    print(*query_params.values())
    stmt = select(*group_bys, *colsToSum.values()).filter_by(global_id=player_id).group_by(*query_params.keys())
    # stmt = select(req_model.time_period, func.sum(req_model.G)).filter(req_model.global_id == player_id).group_by(req_model.time_period)
    # print(stmt)
    data = await db.execute(stmt)
    # ret = [val.__dict__ for val in data.scalars().all()]
    rets = data.all()
    ret = [dict(zip((*query_params.keys(), *colsToSum.keys()), ret)) for ret in rets]
    print(rets)
    # ret_dict = [dict(zip((*group_bys, *colsToSum.values()), ret)) for ret in rets]
    # ret = [req_scheme(*ret) for ret in rets]

    # print(ret)
    return ret

#  TODO: REFACTOR, BITCH!