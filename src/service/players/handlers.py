from typing import Annotated

from fastapi import Depends, Path
from sqlalchemy import select, func

from api.dependencies import db_dep
from service.players.helpers import filter_params_for_where_orm_objects, ModelSchemaHelper


async def get_player_stats_by_metric(
        player_id: int,
        helper_obj: ModelSchemaHelper,
        db: db_dep,
        add_sum_col_names: list[str] | None = None,
        add_group_by_col_names: list[str] | None = None,
        exclude_sum: list[str] | None = None,
        exclude_group: list[str] | None = None
):
    orm_model = helper_obj.orm_model  # получаем ORM-модель алхимии (api.models.player.PlayerPlusminus)
    orm_model_columns = orm_model.get_columns()
    print(f"DEBUUG: orm model :: {orm_model}")
    # print(f"DEBUUG: orm model columns :: {orm_model_columns}")  # поля в api.models.player.PlayerPlusminus
    # print(f"DEBUUG: type of orm model columns :: {[type(i) for i in orm_model_columns]}")
    basic_group_bys = helper_obj.basic_group_bys
    # print(f"DEBUUG helper obj :: {helper_obj}")
    # print(f"DUBUUUG basic group bys :: {basic_group_bys}")
    query_params = helper_obj.validated_query_params
    print(f"DUBUUUG query params :: {query_params}")

    """Тут надо суммировать по всем полям показателей"""
    cols_obj_to_sum = {name: func.sum(col).label(name) for name, col in orm_model.__table__.columns.items() if
                       name in orm_model_columns and name not in exclude_sum}
    print("*************************************************")
    print(f"DEEEBUUUUGGGG: cols_obj_to_sum: {cols_obj_to_sum}")

    # Basic_groupBys - это объекты или имена, по которым обязательно надо группировать, поэтому под них отдельная схема
    basic_groupbys_names = list(basic_group_bys.keys())
    print(f"DEEEBUUUUGGGG: basic_groupbys_names: {basic_groupbys_names}")
    basic_groupbys_obj: list = [getattr(orm_model, param_name) for param_name in basic_group_bys]
    print(f"DEEEBUUUUGGGG: basic_groupbys_obj: {basic_groupbys_obj}")

    # Объекты алхимии для фильтрации
    ands_obj = filter_params_for_where_orm_objects(req_model=orm_model, query_params=query_params, id_filter=player_id)
    print(f"DEEEBUUUUGGGG: ands_obj: {ands_obj}")

    # GroupBy объекты, которые получаем из query параметров запроса (и смотрим, нет ли их в Basic)
    group_bys_query_obj = [getattr(orm_model, param_name) for param_name, param_value in query_params.items()]
    print(f"DEEEBUUUUGGGG: group_bys_query_obj: {group_bys_query_obj}")

    full_groupbys_obj = basic_groupbys_obj + [gr_by for gr_by in group_bys_query_obj if gr_by not in basic_groupbys_obj]
    print(f"DEEEBUUUUGGGG: full_groupbys_obj: {full_groupbys_obj}")

    query_groupbys_names = [param_name for param_name in query_params.keys() if param_name not in basic_groupbys_names]
    print(f"DEEEBUUUUGGGG: query_groupbys_names: {query_groupbys_names}")
    full_groupbys_names = basic_groupbys_names + query_groupbys_names
    print(f"DEEEBUUUUGGGG: full_groupbys_names: {full_groupbys_names}")

    stmt = select(*full_groupbys_obj, *cols_obj_to_sum.values()).where(*ands_obj).group_by(*full_groupbys_names)
    data = await db.execute(stmt)
    data = data.mappings().all()
    print(f"DEEEBUUUUGGGG: data: {data}")

    return data
