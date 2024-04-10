from typing import Annotated, Literal

from fastapi import Query
from pydantic import BaseModel, Field, field_validator


class TeamsParamsValidator:
    # TODO: сделать валидацию по полям + особенно важно обратить внимание на поле club_name
    ...


class TeamsAlwaysGroupBy:
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None


class TeamsTm6Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm6FilteredQuery(TeamsTm6Query):
    pass


class TeamsTm11Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm11FilteredQuery(TeamsTm11Query):
    pass


class TeamsTm14Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm14FilteredQuery(TeamsTm14Query):
    pass


class TeamsTm5Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm5FilteredQuery(TeamsTm5Query):
    pass


class TeamsTm7Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm7FilteredQuery(TeamsTm7Query):
    pass


class TeamsTm20Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm20FilteredQuery(TeamsTm20Query):
    pass


class TeamsTm22Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm22FilteredQuery(TeamsTm22Query):
    pass


class TeamsTm8Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm8FilteredQuery(TeamsTm8Query):
    pass


class TeamsTm12Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm12FilteredQuery(TeamsTm12Query):
    pass


class TeamsTm13Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm13FilteredQuery(TeamsTm13Query):
    pass


class TeamsTm9Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm9FilteredQuery(TeamsTm9Query):
    pass


class TeamsTm17Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm17FilteredQuery(TeamsTm17Query):
    pass


class TeamsTm10Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm10FilteredQuery(TeamsTm10Query):
    pass


class TeamsTm15Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm15FilteredQuery(TeamsTm15Query):
    pass


class TeamsTm16Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm16FilteredQuery(TeamsTm16Query):
    pass


class TeamsTm18Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm18FilteredQuery(TeamsTm18Query):
    pass


class TeamsTm19Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm19FilteredQuery(TeamsTm19Query):
    pass


class TeamsTm21Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm21FilteredQuery(TeamsTm21Query):
    pass


class TeamsTm25Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm25FilteredQuery(TeamsTm25Query):
    pass


class TeamsTm1Query(TeamsAlwaysGroupBy, BaseModel):
    pass


class TeamsTm1FilteredQuery(TeamsTm1Query):
    pass


