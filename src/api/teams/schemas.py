from typing import Literal

from pydantic import BaseModel


class TeamsParamsValidator:
    # TODO: сделать валидацию по полям + особенно важно обратить внимание на поле club_name
    ...


class TeamsAlwaysGroupBy(BaseModel):
    league: Literal['khl', 'mhl', 'whl', 'vhl', None] = None
    tnt_id: int | None = None
    tnt_type: Literal['r', 'p', 'n', None] = None


class TeamsTm6Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm6FilteredQuery(TeamsTm6Query):
    pass


class TeamsTm11Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm11FilteredQuery(TeamsTm11Query):
    pass


class TeamsTm14Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm14FilteredQuery(TeamsTm14Query):
    pass


class TeamsTm5Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm5FilteredQuery(TeamsTm5Query):
    pass


class TeamsTm7Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm7FilteredQuery(TeamsTm7Query):
    pass


class TeamsTm20Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm20FilteredQuery(TeamsTm20Query):
    pass


class TeamsTm22Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm22FilteredQuery(TeamsTm22Query):
    pass


class TeamsTm8Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm8FilteredQuery(TeamsTm8Query):
    pass


class TeamsTm12Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm12FilteredQuery(TeamsTm12Query):
    pass


class TeamsTm13Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm13FilteredQuery(TeamsTm13Query):
    pass


class TeamsTm9Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm9FilteredQuery(TeamsTm9Query):
    pass


class TeamsTm17Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm17FilteredQuery(TeamsTm17Query):
    pass


class TeamsTm10Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm10FilteredQuery(TeamsTm10Query):
    pass


class TeamsTm15Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm15FilteredQuery(TeamsTm15Query):
    pass


class TeamsTm16Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm16FilteredQuery(TeamsTm16Query):
    pass


class TeamsTm18Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm18FilteredQuery(TeamsTm18Query):
    pass


class TeamsTm19Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm19FilteredQuery(TeamsTm19Query):
    pass


class TeamsTm21Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm21FilteredQuery(TeamsTm21Query):
    pass


class TeamsTm25Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm25FilteredQuery(TeamsTm25Query):
    pass


class TeamsTm1Query(TeamsAlwaysGroupBy):
    pass


class TeamsTm1FilteredQuery(TeamsTm1Query):
    pass


