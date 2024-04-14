from typing import Literal

from pydantic import BaseModel, field_validator


class ArenasParamsValidator:
    pass
    # @field_validator('time_period', check_fields=False)
    # @classmethod
    # def valid_period_number(cls, val: list[int] | int | None):
    #     possible_values = [1, 2, 3, 4, 50, None]
    #     if isinstance(val, list):
    #         for v in val:
    #             if v not in possible_values:
    #                 raise ValueError('should be one of [1, 2, 3, 4, 50]')
    #     else:
    #         if val not in possible_values:
    #             raise ValueError('should be one of [1, 2, 3, 4, 50]')
    #     return val
    #
    # @field_validator('team_status', check_fields=False)
    # @classmethod
    # def valid_team_status(cls, val: list[str] | int | None):
    #     possible_values = ['pp', 'sh', 'eq']
    #     if isinstance(val, list):
    #         for v in val:
    #             if v not in possible_values:
    #                 raise ValueError('should be one of [pp, sh, eq]')
    #     else:
    #         if val not in possible_values:
    #             raise ValueError('should be one of [pp, sh, eq]')
    #     return val


class ArenasTntQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None


class ArenasTntFilteredQuery(ArenasTntQuery):
    pass


class ArenasGamesQuery(ArenasTntQuery):
    pass


class ArenasGamesFilteredQuery(ArenasGamesQuery):
    pass
