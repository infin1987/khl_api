from typing import Annotated, Literal

from fastapi import Query
from pydantic import BaseModel, Field, field_validator


class TeamsParamsValidator:
    ...


class TeamsTm6Query(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None


class TeamsTm6FilteredQuery(TeamsTm6Query):
    pass
