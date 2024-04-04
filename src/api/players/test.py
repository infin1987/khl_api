from typing import Annotated, Literal

from fastapi import Query
from pydantic import BaseModel, Field, field_validator


class PlayersParamsValidator:

    @field_validator('time_period', check_fields=False)
    @classmethod
    def valid_period_number(cls, val: list[int] | int | None):
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


class PlayersAssistsQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersShotattemptsFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    time_period: Annotated[list[int] | int | None, Query()] = None
    team_status: Annotated[list[str] | str | None, Query()] = None
    net: Literal['en', 'eno', 'enb', 'gk', None] = None

'''
class PlayersShotattemptsFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None
    time_period: Annotated[list[int] | int | None, Query()] = None
    team_status: Annotated[list[str] | str | None, Query()] = None
    net: Literal['en', 'eno', 'enb', 'gk', None] = None
'''

query_params = {'tnt_id': '202', 'time_period': '2', 'tnt_type': 'r', 'league': 'khl', 'net': 'en'}
all_needed_params = list(PlayersShotattemptsFilteredQuery.__fields__.keys())

for param in query_params:
    if param not in all_needed_params:
        raise ValueError(f'{param} :: this parameter is not valid, try these: {all_needed_params}')

print(f"Валидируем квери параметры из запроса по модели PlayersShotattemptsFilteredQuery: {PlayersShotattemptsFilteredQuery.model_validate(query_params)}")