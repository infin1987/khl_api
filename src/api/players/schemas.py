from enum import Enum
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
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersShotsFilteredQuery(PlayersShotsQuery, PlayersParamsValidator):
    time_period: Annotated[list[int] | int | None, Query()] = None
    team_status: Annotated[list[str] | str | None, Query()] = None
    net: Literal['en', 'eno', 'enb', 'gk', None] = None


class PlayersTotalResponse(BaseModel):

    global_id: int
    max_ts: int
    tnt_id: int
    team_id: int
    playername: str
    position: str
    clid: int
    team_name: str
    season: str
    league: str
    tnt_type: str

    GP: int
    G: int
    A: int
    P: int
    PIM: int
    pm: int

    EVG: int
    PPG: int
    SHG: int
    OTG: int
    first_g: int
    GWG: int
    GWS: int
    plus: int
    minus: int
    toi_avg: str
    pptoi_avg: str
    shtoi_avg: str
    eqtoi_avg: str
    entoi_avg: str
    ppsft_avg: float
    shsft_avg: float
    eqsft_avg: float
    ensft_avg: float
    sft_avg: float
    FO: int
    FOW: int
    fo_pct: float
    FoA: int
    TkA: int
    Hits: int
    P_Intc: int
    S: int
    SOG: int
    sog_pct: float
    sog_avg: float
    toa_avg: str


class PlayersAssistsQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersAssistsFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    time_period: Annotated[list[int] | int | None, Query()] = None
    team_status: Annotated[list[str] | str | None, Query()] = None
    net: Literal['en', 'eno', 'enb', 'gk', None] = None


class PlayersPointsQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersPointsFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    time_period: Annotated[list[int] | int | None, Query()] = None
    team_status: Annotated[list[str] | str | None, Query()] = None
    net: Literal['en', 'eno', 'enb', 'gk', None] = None


class PlayersFaceoffsQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersFaceoffsFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    time_period: Annotated[list[int] | int | None, Query()] = None
    team_status: Annotated[list[str] | str | None, Query()] = None
    net: Literal['en', 'eno', 'enb', 'gk', None] = None


class PlayersActivityQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersActivityFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    time_period: Annotated[list[int] | int | None, Query()] = None
    team_status: Annotated[list[str] | str | None, Query()] = None
    net: Literal['en', 'eno', 'enb', 'gk', None] = None


class PlayersBullitsQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersBullitsFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    pass


class PlayersPlusminusQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersPlusminusFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    time_period: Annotated[list[int] | int | None, Query()] = None
    team_status: Annotated[list[str] | str | None, Query()] = None
    net: Literal['en', 'eno', 'enb', 'gk', None] = None


class PlayersToiQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersToiFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    pass


class PlayersToadQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersToadFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    pass


class PlayersShotattemptsQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersShotattemptsFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    time_period: Annotated[list[int] | int | None, Query()] = None
    team_status: Annotated[list[str] | str | None, Query()] = None
    net: Literal['en', 'eno', 'enb', 'gk', None] = None


class PlayersSatQuery(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None
    position: str | None = None


class PlayersSatFilteredQuery(PlayersAssistsQuery, PlayersParamsValidator):
    pass
