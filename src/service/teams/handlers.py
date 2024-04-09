from sqlalchemy import select, func
from error_handling_config import _error, _debug, _info, _warning

from api.dependencies import db_dep
from service.teams.helpers import ModelSchemaHelperTeams as ModelSchemaHelper


async def get_team_stats_by_metric(
        club_name: str,
        helper_obj: ModelSchemaHelper,
        db: db_dep,
):
    orm_model = helper_obj.orm_model  # получаем ORM-модель алхимии (api.models.player.PlayerPlusminus)
    orm_model_columns = orm_model.get_columns()
    _debug(f"orm model :: {orm_model}")
    _debug(f"Pisyat dva :: {orm_model.__table__.columns.items()}")
    basic_group_bys = helper_obj.basic_group_bys
    query_params = helper_obj.validated_query_params
    _debug(f"query params :: {query_params}")

    if "time_period" in query_params.keys() or "net" in query_params.keys():
        """Тут надо суммировать по всем полям показателей"""
        cols_obj_to_sum = {name: func.sum(col).label(name) for name, col in orm_model.__table__.columns.items() if
                           name in orm_model_columns}
        print("*************************************************")
        _debug(f"cols_obj_to_sum: {cols_obj_to_sum}")

        # Basic_groupBys - это объекты или имена, по которым обязательно надо группировать, поэтому под них отдельная схема
        basic_groupbys_names = list(basic_group_bys.keys())
        _debug(f"basic_groupbys_names: {basic_groupbys_names}")
        basic_groupbys_obj: list = [getattr(orm_model, param_name) for param_name in basic_group_bys]
        _debug(f"basic_groupbys_obj: {basic_groupbys_obj}")

        # Объекты алхимии для фильтрации
        ands_obj = helper_obj.filter_params_for_where_orm_objects(query_params=query_params, id_filter=club_name)
        # _debug(f"ands_obj: {ands_obj[2]}")

        # GroupBy объекты, которые получаем из query параметров запроса (и смотрим, нет ли их в Basic)
        group_bys_query_obj = [getattr(orm_model, param_name) for param_name, param_value in query_params.items()]
        # _debug(f"group_bys_query_obj: {group_bys_query_obj[0]}")

        full_groupbys_obj = basic_groupbys_obj + [gr_by for gr_by in group_bys_query_obj if gr_by not in basic_groupbys_obj]
        # _debug(f"full_groupbys_obj: {full_groupbys_obj[0]}")

        query_groupbys_names = [param_name for param_name in query_params.keys() if param_name not in basic_groupbys_names]
        _debug(f"query_groupbys_names: {query_groupbys_names}")
        full_groupbys_names = basic_groupbys_names + query_groupbys_names
        _debug(f"full_groupbys_names: {full_groupbys_names}")

        stmt = select(*full_groupbys_obj, *cols_obj_to_sum.values()).where(*ands_obj).group_by(*full_groupbys_names)
        data = await db.execute(stmt)
        data = data.mappings().all()
        _debug(f"data: {data}")
        return data

    else:
        # Объекты алхимии для фильтрации
        ands_obj = helper_obj.filter_params_for_where_orm_objects(query_params=query_params, id_filter=club_name)
        _debug(f"ands_obj: {ands_obj}")

        stmt = select(orm_model).where(*ands_obj)
        data = await db.execute(stmt)
        data = data.scalars().all()
        _debug(f"data: {data}")
        return data

