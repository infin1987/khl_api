from fastapi import APIRouter
from .players.routers import players_router
from .teams.routers import teams_router

main_stats_router = APIRouter()
main_stats_router.include_router(players_router)
main_stats_router.include_router(teams_router)
#
# def get_model_by_metric(tablename: str):
#     for elem in Base.registry.mappers:
#         if elem.entity.__tablename__ == tablename:
#             return elem.entity
#
#
# def get_schema_by_metric(metric: str):
#     return getattr(api_schemas, f'Player{metric.capitalize()}FilteredQuery')
#
# def get_basic_groupby_schema_by_metric(schema):
#     return schema.__bases__[0]
#
# def get_proper_orm_model(
#         metric: Annotated[str, Path()],
#         league: str | None = None,
#         tnt_id: int | None = None,
#         tnt_type: str | None = None,
#         time_period: int | None = None,
#         team_status: str | None = None,
#         net: str | None = None,
#         position: str | None = None,
# ) -> PlayerGoals | PlayerGoalsFilter:
#     params = league, tnt_id, tnt_type, time_period, team_status, net, position
#     tablename = f'pl_{metric}_api_filters' if any(params) else f'pl_{metric}_api'
#     return get_model_by_metric(tablename)
#
#
# @main_stats_router.get('/{player_id}/metrics/{metric}/all')
# # async def secured_data(token: oauth2_dep, db: db_dep):
# async def player_all_stats_by_metric(
#         player_id: Annotated[int, Path()],
#         # metric: Annotated[str, Path()],
#         # query: Annotated[list, Depends()],
#         req_model: Annotated[PlayerGoals | PlayerGoalsFilter, Depends(get_proper_orm_model)],
#         db: db_dep,
#         last_updated: Annotated[int, Header()],
#         request: Request
# ):
#     stmt = select(req_model).where(req_model.global_id == player_id).order_by(desc(req_model.tnt_id))
#     data = await db.execute(stmt)
#     # ret = [val.__dict__ for val in data.scalars().all()]
#     return data.scalars().all()
#
#
# @main_stats_router.get('/{player_id}/metrics/{metric}/')
# # async def secured_data(token: oauth2_dep, db: db_dep):
# async def player_stats_by_metric(
#         player_id: Annotated[int, Path()],
#         metric: Annotated[str, Path()],
#         # query: Annotated[list, Depends()],
#         req_model: Annotated[PlayerMetricFilteredMixin, Depends(get_proper_orm_model)],
#         db: db_dep,
#         last_updated: Annotated[int, Header()],
#         request: Request
# ):
#     print(last_updated, req_model, request.url)
#     last_updated_cache = 20221200
#     if last_updated > last_updated_cache:
#         raise no_new_data_exception
#     """Тут надо суммировать по всем полям показателей"""
#     req_scheme = get_schema_by_metric(metric)
#     cols_obj_to_sum = {name: func.sum(col).label(name) for name, col in req_model.__table__.columns.items() if name in req_model.get_columns()}
#
#     query_params_multi = {}
#     for k, v in request.query_params.multi_items():
#         if k in query_params_multi:
#             old_value = query_params_multi[k]
#             new_val = old_value + [v] if isinstance(old_value, list) else [old_value, v]
#             query_params_multi[k] = new_val
#         else:
#             query_params_multi[k] = v
#
#     query_params = {k: v for k, v in req_scheme.model_validate(query_params_multi) if v}
#     basic_groupbys_scheme = get_basic_groupby_schema_by_metric(req_scheme)
#     print(req_scheme.__bases__)
#
#     basic_groupbys: dict = basic_groupbys_scheme.model_validate(query_params).model_dump()
#     basic_groupbys_names = list(basic_groupbys.keys())
#     basic_groupbys_obj: list = [getattr(req_model, param_name) for param_name in basic_groupbys]
#
#     ands = [req_model.global_id == player_id,]
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
#     rets = data.all()
#     # print(rets)
#     ret = [dict(zip((*full_groupbys_names, *cols_obj_to_sum.keys()), ret)) for ret in rets]
#
#     return ret
#
# #  TODO: REFACTOR, BITCH!