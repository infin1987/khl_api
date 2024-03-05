from typing import Annotated, Literal

from pydantic import BaseModel, Field


class PlayerGoalsQuery(BaseModel):
    __tp__ = 'goals'
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', None] = None
    # team_status: str | None = None
    # net: str | None = None
    position: str | None = None

class PlayerGoalsFilteredQuery(PlayerGoalsQuery):
    # league: str | None = None
    # tnt_id: int | None = None
    # tnt_type: str | None = None
    time_period: int | None = None
    # period: int = Field(alias='time_period', default=None)
    team_status: str | None = None
    net: str | None = None
    # position: str | None = None

class PlayerPenaltiesQuery(PlayerGoalsQuery):
    __tp__ = 'penalties'

class PlayerPenaltiesFilteredQuery(PlayerPenaltiesQuery):
    pass