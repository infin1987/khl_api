from typing import Annotated, Literal
import sys
from error_handling_config import _error, _debug, _info, _warning

from fastapi import Path, Header, Request, HTTPException, Depends
from pydantic import BaseModel, ValidationError
from db.api.config import Base
from api.trainers import schemas as trainers_schemas
from service.arenas.helpers import ModelSchemaHelper as ModelSchemaBase

class ModelSchemaHelper(ModelSchemaBase):

    def get_schema_by_metric(self) -> BaseModel:
        module = getattr(sys.modules[__name__], f'{self.name.lower()}_schemas')
        return getattr(module, f'{self.name.capitalize()}{self.metric.capitalize()}FilteredQuery')


async def get_helper_obj(
        # schedule_id: Annotated[int, Path()],
        request: Request):
    yield ModelSchemaHelper('trainers', 'trainer', 'games', request)


async def get_helper_nometric_obj(
        # metric: Annotated[Literal[*metrics], Path()],
        request: Request):
    yield ModelSchemaHelper('trainers', 'trainer', 'tnt', request)


helper_dep = Annotated[ModelSchemaHelper, Depends(get_helper_obj)]
helper_nometric_dep = Annotated[ModelSchemaHelper, Depends(get_helper_nometric_obj)]

