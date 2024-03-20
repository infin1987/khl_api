from enum import Enum
from typing import Annotated, Literal

from fastapi import Query
from pydantic import BaseModel, Field, field_validator


class PlayersParamsValidator:

    @field_validator('time_period', check_fields=False)
    @classmethod
    def valid_period_number(cls, val: list[int] | int| None):
        possible_values = [1, 2, 3, 4, 50, None]
        if isinstance(val, list):
            for v in val:
                if v not in possible_values:
                    raise ValueError('should be one of [1, 2, 3, 4, 50]')
        else:
            if val not in possible_values:
                raise ValueError('should be one of [1, 2, 3, 4, 50]')
        return val

    @field_validator('team_status', check_fields=False)
    @classmethod
    def valid_team_status(cls, val: list[str] | int | None):
        possible_values = ['pp', 'sh', 'eq']
        if isinstance(val, list):
            for v in val:
                if v not in possible_values:
                    raise ValueError('should be one of [pp, sh, eq]')
        else:
            if val not in possible_values:
                raise ValueError('should be one of [pp, sh, eq]')
        return val


class PlayersGoalsQuery(BaseModel):
    # __tp__ = 'goals'
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersGoalsFilteredQuery(PlayersGoalsQuery, PlayersParamsValidator):
    time_period: Annotated[list[int] | int | None, Query()] = None
    team_status: Annotated[list[str] | str | None, Query()] = None
    net: Literal['en', 'eno', 'enb', 'gk', None] = None


class PlayersPenaltiesQuery(PlayersGoalsQuery):
    pass


class PlayersPenaltiesFilteredQuery(PlayersPenaltiesQuery, PlayersParamsValidator):
    time_period: Annotated[list[int] | int | None, Query()] = None


class PlayersShotsQuery(PlayersGoalsQuery):
    pass


class PlayersShotsFilteredQuery(PlayersShotsQuery, PlayersParamsValidator):
    pass