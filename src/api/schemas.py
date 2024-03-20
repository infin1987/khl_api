from enum import Enum
from typing import Annotated, Literal

from fastapi import Query
from pydantic import BaseModel, Field

class BaseGroupBy(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', None] = None

# class PlayersGoalsQuery(BaseModel):
#     # __tp__ = 'goals'
#     league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
#     tnt_id: int | None = None
#     tnt_type: Literal['r', 'p', None] = None
#     # team_status: str | None = None
#     # net: str | None = None
#     position: str | None = None
#
# class Period(int, Enum):
#     first = 1
#     second = 2
#     third = 3
#     OT = 4
#
#
# class PlayersGoalsFilteredQuery(PlayersGoalsQuery):
#     # league: str | None = None
#     # tnt_id: int | None = None
#     # tnt_type: str | None = None
#     time_period: Period | list[Period] | None = None
#     time_period: Annotated[list[Period] | Period | None, Query()] = None
#     time_period: Annotated[list[int] | int | None, Query()] = None
#     # time_period: int | None = None
#     # period: int = Field(alias='time_period', default=None)
#     team_status: str | None = None
#     team_status: list[str] | str | None = None
#     net: Literal['en', 'eno', 'enb', 'gk', None] = None
#     # position: str | None = None
#
#
# class PlayersPenaltiesQuery(PlayersGoalsQuery):
#     __tp__ = 'penalties'
#
# class PlayersGoalsFilteredQuery(PlayersPenaltiesQuery):
#     pass
