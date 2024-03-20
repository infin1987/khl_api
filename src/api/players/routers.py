from typing import Annotated

from fastapi import APIRouter, Query, Request, Header, Path, Depends
from sqlalchemy import select, func, desc

from api.dependencies import db_dep
from api.players.schemas import PlayersGoalsQuery
from db.api.models.player import PlayersBio, PlayersGoals, PlayersGoalsFilter, PlayersMetricFilteredMixin, PlayersTotal
from db.api.models.tournaments import Tournaments
from exceptions import no_new_data_exception
from service.helpers import check_last_updated
from service.players.handlers import get_player_stats_by_metric

from service.players.helpers import (get_schema_by_metric, get_proper_orm_model, get_basic_groupby_schema,
                                     ModelSchemaHelper)


players_router = APIRouter(prefix='/players', tags=['players'], dependencies=[Depends(check_last_updated)])

helper_dep = Annotated[ModelSchemaHelper, Depends(ModelSchemaHelper('players', 'pl'))]

@players_router.get('/test/{player_id}/{metric}')
async def get_players(q: Request,
                      player_id: int,
                      # tnt_id: int | None,
                      # obj: Annotated[ModelSchemaHelper, Depends(helper)]
                      obj: helper_dep
                      ):
    print(obj)
    print(type(q.query_params))
    print(q.query_params.items())
    print(q.query_params.multi_items(), q.query_params.getlist('q'))
    # d = {key: value if key in d elsfor key, value in q.query_params.multi_items()}
    d = {}
    for k, v in q.query_params.multi_items():
        print(k, v)
        if k in d:
            print([*(d[k],)] + [v])
            d[k] = [*(d[k],)] + [v]
        else:
            d[k] = v

    print(d)
    for key, val in q.query_params.multi_items():
        print(key, val)
    return {'data': 'here should be some data'}
    # PlayerGoalsFilteredQuery.model_validate(q.query_params.multi_items())


@players_router.get('/stats')
async def get_players_filtered(q: str):
    return {'data': 'all players filered data'}


@players_router.get('')
async def get_players_bio(
        db: db_dep,
        tnt_id: Annotated[str | None, Query()] = None,
):
    data = await db.execute(select(PlayersBio))
                            # .where(PlayersBio.tnt_id == tnt_id))
    ret = data.scalars().all()
    print(len(ret))
    return ret

@players_router.get('/total')
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


@players_router.get('/{player_id}/metrics/{metric}/all')
# async def secured_data(token: oauth2_dep, db: db_dep):
async def player_all_stats_by_metric(
        player_id: Annotated[int, Path()],
        helper_obj: helper_dep,
        db: db_dep,
):
    orm_model = helper_obj.orm_model
    stmt = select(orm_model).where(orm_model.global_id == player_id).order_by(desc(orm_model.tnt_id))
    data = await db.execute(stmt)
    # ret = [val.__dict__ for val in data.scalars().all()]
    return data.scalars().all()


# @players_router.get('/{player_id}/metrics/{metric}/')
# # async def secured_data(token: oauth2_dep, db: db_dep):
# async def player_stats_by_metric(
#         player_id: Annotated[int, Path()],
#         metric: Annotated[str, Path()],
#         # query: Annotated[list, Depends()],
#         req_model: Annotated[PlayerMetricFilteredMixin, Depends(get_proper_orm_model)],
#         db: db_dep,
#         request: Request,
#         # obj: Annotated[object, Depends(helper)]
# ):
#     print(req_model, request.url)
#
#     """Тут надо суммировать по всем полям показателей"""
#     req_scheme = get_schema_by_metric(metric)
#     cols_obj_to_sum = {name: func.sum(col).label(name) for name, col in req_model.__table__.columns.items() if
#                        name in req_model.get_columns()}
#
#     query_params_multi = {}
#     print(request.query_params.multi_items())
#     for k, v in request.query_params.multi_items():
#         if k in query_params_multi:
#             old_value = query_params_multi[k]
#             new_val = old_value + [v] if isinstance(old_value, list) else [old_value, v]
#             query_params_multi[k] = new_val
#         else:
#             query_params_multi[k] = v
#
#     query_params = {k: v for k, v in req_scheme.model_validate(query_params_multi) if v}
#     basic_groupbys_scheme = get_basic_groupby_schema(req_scheme)
#     print(req_scheme.__bases__)
#
#     basic_groupbys: dict = basic_groupbys_scheme.model_validate(query_params).model_dump()
#     basic_groupbys_names = list(basic_groupbys)
#     basic_groupbys_obj: list = [getattr(req_model, param_name) for param_name in basic_groupbys]
#
#     ands = [req_model.global_id == player_id, ]
#     for param_name, param_value in query_params.items():
#         if isinstance(param_value, list):
#             ands.append(getattr(req_model, param_name).in_(param_value))
#         else:
#             ands.append(getattr(req_model, param_name) == param_value)
#
#     group_bys_query = [getattr(req_model, param_name) for param_name, param_value in query_params.items()]
#
#     full_groupbys_obj = basic_groupbys_obj + [gr_by for gr_by in group_bys_query if gr_by not in basic_groupbys_obj]
#
#     query_groupbys_names = [param_name for param_name in query_params.keys() if param_name not in basic_groupbys_names]
#     full_groupbys_names = basic_groupbys_names + query_groupbys_names
#
#     stmt = select(*full_groupbys_obj, *cols_obj_to_sum.values()).where(*ands).group_by(*full_groupbys_names)
#     data = await db.execute(stmt)
#     data = data.mappings().all()
#     # print(rets[0]._asdict())
#     # print(rets)
#     # rets = [ret._asdict() for ret in rets]
#     # print(ret)
#     # ret = [dict(zip((*full_groupbys_names, *cols_obj_to_sum.keys()), ret)) for ret in rets]
#
#     return data
