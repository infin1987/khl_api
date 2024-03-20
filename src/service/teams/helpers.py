from typing import Annotated, Any, Union, Literal
import sys

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
metrics = ['goals', 'penalties', 'shots', 'faceoffs', 'attendance']

def get_model_by_metric(tablename: str):
    for elem in Base.registry.mappers:
        if elem.entity.__tablename__ == tablename:
            return elem.entity


def get_schema_by_metric(metric: str):
    return getattr(players_schemas, f'Player{metric.capitalize()}FilteredQuery')


def get_basic_groupby_schema(schema):
    return schema.__bases__[0]


def get_proper_orm_model(
        metric: Annotated[str, Path()],
        league: str | None = None,
        tnt_id: int | None = None,
        tnt_type: str | None = None,
        time_period: int | None = None,
        team_status: str | None = None,
        net: str | None = None,
        position: str | None = None,
) -> PlayersGoals | PlayersGoalsFilter:
    params = league, tnt_id, tnt_type, time_period, team_status, net, position
    tablename = f'pl_{metric}_api_filters' if any(params) else f'pl_{metric}_api'
    return get_model_by_metric(tablename)


def get_query_params(request: Request) -> dict:
    query_params_multi = {}
    print(request.query_params.multi_items())
    for k, v in request.query_params.multi_items():
        if k in query_params_multi:
            old_value = query_params_multi[k]
            new_val = old_value + [v] if isinstance(old_value, list) else [old_value, v]
            query_params_multi[k] = new_val
        else:
            query_params_multi[k] = v
    return query_params_multi


def filter_params_for_where_orm_objects(
        req_model,
        query_params: dict,
        id_filter: int
) -> list:
    ands = [req_model.global_id == id_filter, ]
    # TODO: default and плохой, много где не будет global_id - переделать
    for param_name, param_value in query_params.items():
        if isinstance(param_value, list):
            ands.append(getattr(req_model, param_name).in_(param_value))
        else:
            ands.append(getattr(req_model, param_name) == param_value)
    return ands


class ModelSchemaHelper:

    # TODO: Можно добавить метод, который в зависимости от метрики будет добавлять еще параметров в group_by и сумму

    def __init__(self, name: str, short_name: str):
        self.name = name
        self.short_name = short_name

    @staticmethod
    def get_query_params(request: Request) -> dict:
        query_params_multi = {}
        print(request.query_params.multi_items())
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
    ) -> Base:
        params = league, tnt_id, tnt_type, time_period, team_status
        tablename = f'{self.short_name}_{metric}_api_filters' if any(params) else f'{self.short_name}_{metric}_api'
        return self.get_orm_model_by_metric(tablename)

    @staticmethod
    def get_orm_model_by_metric(tablename: str) -> Base:
        for elem in Base.registry.mappers:
            if elem.entity.__tablename__ == tablename:
                return elem.entity

    def get_schema_by_metric(self) -> BaseModel:
        module = getattr(sys.modules[__name__], f'{self.name.lower()}_schemas')
        return getattr(module, f'{self.name.capitalize()}{self.metric.capitalize()}FilteredQuery')

    def get_basic_groupby_schema(self) -> BaseModel:
        return self.schema.__bases__[0]

    def __call__(self,
                 metric: Annotated[Literal[*metrics], Path()],
                 request: Request
                 ):
        try:
            self.metric = metric
            self.schema = self.get_schema_by_metric()
            self._basic_group_by_schema = self.get_basic_groupby_schema()
            self._query_params = self.get_query_params(request=request)
            self.validated_query_params = {k: v for k, v in self.schema.model_validate(self._query_params) if v}
            self.orm_model = self.get_orm_model(metric=metric, **self.validated_query_params)
            self.basic_group_bys = self._basic_group_by_schema.model_validate(self.validated_query_params).model_dump()
        except ValidationError as e:
            ers = e.errors()
            for error in ers:
                if error['type'] == 'value_error':
                    error['ctx']['error'] = error['msg']
            raise HTTPException(status_code=400, detail=ers)
        except AttributeError as ae:
            print(ae)
            raise HTTPException(status_code=400, detail='Wrong metric name')
        return self

    def __repr__(self):
        return f'<{self.__class__}, {self.__dict__}'
