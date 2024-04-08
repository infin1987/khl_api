from typing import Annotated, Any, Union, Literal
import sys
from error_handling_config import _error, _debug, _info, _warning

from fastapi import Path, Header, Request, HTTPException, Depends
from pydantic import BaseModel, ValidationError
from starlette.responses import JSONResponse

from api.players.schemas import PlayersGoalsFilteredQuery, PlayersGoalsQuery
from db.api.config import Base
from api.players import schemas as players_schemas
from db.api.models.player import PlayersGoals, PlayersGoalsFilter
from auth.dependencies import rcache_dep
import json, pickle

from exceptions import no_new_data_exception

metrics = ['goals', 'penalties', 'shots', 'faceoffs', 'assists',
           'points', 'activity', 'bullits', 'plusminus', 'toi', 'toad', 'shotattempts', 'sat']


class ModelSchemaHelper:

    # TODO: Можно добавить метод, который в зависимости от метрики будет добавлять еще параметров в group_by и сумму

    def __init__(self, name: str, short_name: str, metric: str, request: Request):
        self.name = name
        self.short_name = short_name
        self.populate_with_params(metric, request)

    def filter_params_for_where_orm_objects(
            self,
            query_params: dict,
            id_filter: int
    ) -> list:
        ands = [self.orm_model.global_id == id_filter, ]
        # TODO: default and плохой, много где не будет global_id - переделать
        for param_name, param_value in query_params.items():
            if isinstance(param_value, list):
                ands.append(getattr(self.orm_model, param_name).in_(param_value))
            else:
                ands.append(getattr(self.orm_model, param_name) == param_value)
        return ands

    @staticmethod
    def get_query_params(request: Request) -> dict:
        query_params_multi = {}
        # print(request.query_params.multi_items())
        for k, v in request.query_params.multi_items():
            if k in query_params_multi:
                old_value = query_params_multi[k]
                new_val = old_value + [v] if isinstance(old_value, list) else [old_value, v]
                query_params_multi[k] = new_val
            else:
                query_params_multi[k] = v
        return query_params_multi

    def get_orm_model(
            self,
            metric: str | None = None,
            league: str | None = None,
            tnt_id: int | None = None,
            tnt_type: str | None = None,
            time_period: int | None = None,
            team_status: str | None = None,
            net: str | None = None,
            position: str | None = None,
            request: Request = None,
    ) -> Base:
        """
        Кроме аргументов выше, передаем в 153 строке (self.orm_model) словарь аргументов
        с провалидированнымим квери параметрами
        """
        # params = league, tnt_id, tnt_type, time_period, team_status, net, position
        params = time_period, team_status, net
        tablename = f'{self.short_name}_{metric}_api_filters' if any(params) else f'{self.short_name}_{metric}_api'
        print(f"FFFFFFFFFFFFFFF: {tablename}")
        return self.get_orm_model_by_metric(tablename)

    @staticmethod
    def get_orm_model_by_metric(tablename: str) -> Base:
        # print(f"FFFFFFFFFFFFFF 2222F: {Base.registry.mappers}")
        for elem in Base.registry.mappers:
            # print(elem.entity.__tablename__)
            if elem.entity.__tablename__ == tablename:
                return elem.entity

    def get_schema_by_metric(self) -> BaseModel:
        module = getattr(sys.modules[__name__], f'{self.name.lower()}_schemas')
        return getattr(module, f'{self.name.capitalize()}{self.metric.capitalize()}FilteredQuery')

    def get_basic_groupby_schema(self) -> BaseModel:
        return self.schema.__bases__[0]

    def populate_with_params(self,
                             metric: str,
                             request: Request
                             ):
        try:
            self.metric = metric
            self.schema = self.get_schema_by_metric()  # <class 'api.players.schemas.PlayersSatFilteredQuery'>
            self._basic_group_by_schema = self.get_basic_groupby_schema()  # в схемах --> PlayersAssistsQuery
            self._query_params = self.get_query_params(request=request)  # квери параметры из запроса {'tnt_id': '245'}

            """
            Проверяем, корректны ли все квери параметры (есть ли они вообше в схеме)
            """
            all_needed_params = list(self.schema.__fields__.keys())
            for param in self._query_params:
                if param not in all_needed_params:
                    _error(f'Wrong parameter ({param}) doesn\'t exist. Uses '
                           f'one of these: {all_needed_params}')
                    raise HTTPException(status_code=404,
                                        detail=f'Wrong parameter ({param}) :: doesn\'t exist. Uses '
                                               f'one of these: {all_needed_params}')
            # TODO: REFACTOR BITCH!
            """
            Валидируем параметры и создаем словарь из них - validated_query_params
            """
            self.validated_query_params = {k: v for k, v in self.schema.model_validate(self._query_params) if v}
            self.orm_model = self.get_orm_model(metric=metric, **self.validated_query_params, request=request)
            print(f"OOOOOOOOOOOOOORRRRRRRRRRRRM: {self.orm_model}")
            self.basic_group_bys = self._basic_group_by_schema.model_validate(self.validated_query_params).model_dump()
        except ValidationError as e:
            ers = e.errors()
            for error in ers:
                if error['type'] == 'value_error':
                    error['ctx']['error'] = error['msg']
            _error(f"ValidationError --> {ers}")
            raise HTTPException(status_code=400, detail=ers)
        except AttributeError as ae:
            _error(f"error in helpers.populate_with_params (AttributeError) :: Wrong metric name --> {ae}")
            raise HTTPException(status_code=400, detail='Wrong metric name')

    def __repr__(self):
        return f'<{self.__class__}, {self.__dict__}>'


async def get_helper_obj(
        metric: Annotated[Literal[*metrics], Path()],
        request: Request):
    yield ModelSchemaHelper('players', 'pl', metric, request)


helper_dep = Annotated[ModelSchemaHelper, Depends(get_helper_obj)]
