from typing import Annotated, Any, Union, Literal
import sys

from fastapi import Path, Header, Request, HTTPException, Depends
from pydantic import BaseModel, ValidationError

from api.teams import schemas as teams_schemas
from db.api.config import Base
from service.players.helpers import ModelSchemaHelper

# metrics = [f"TM{i}" for i in range(1, 26)]
metrics = ["TM6"]

class ModelSchemaHelperTeams(ModelSchemaHelper):
    def filter_params_for_where_orm_objects(
            self,
            query_params: dict,
            id_filter: int
    ) -> list:
        ands = [self.orm_model.club_name == id_filter, ]
        # TODO: default and плохой, много где не будет global_id - переделать
        for param_name, param_value in query_params.items():
            if isinstance(param_value, list):
                ands.append(getattr(self.orm_model, param_name).in_(param_value))
            else:
                ands.append(getattr(self.orm_model, param_name) == param_value)
        return ands

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

async def get_helper_obj(
        metric: Annotated[Literal[*metrics], Path()],
        request: Request):
    yield ModelSchemaHelperTeams('teams', 'team', metric, request)


helper_dep = Annotated[ModelSchemaHelperTeams, Depends(get_helper_obj)]
