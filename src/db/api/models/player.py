from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column

from db.api.config import Base


class PlayerMetricMixin:
    global_id: Mapped[int] = mapped_column(primary_key=True)
    max_ts: Mapped[int] = mapped_column(primary_key=True)
    tnt_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    team_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    playername: Mapped[str] = mapped_column(nullable=False)
    position: Mapped[str] = mapped_column(nullable=False)
    clid: Mapped[int] = mapped_column(nullable=False)
    team_name: Mapped[str] = mapped_column(nullable=False)
    season: Mapped[str] = mapped_column(nullable=False)
    league: Mapped[str] = mapped_column(nullable=False)
    tnt_type: Mapped[str] = mapped_column(nullable=False)


class PlayerMetricFilteredMixin(PlayerMetricMixin):
    time_period: Mapped[int] = mapped_column(nullable=True)
    team_status: Mapped[str] = mapped_column(nullable=True)
    net: Mapped[str] = mapped_column(nullable=True)


class PlayerGoalsParamsAllMixin:
    GP: Mapped[int] = mapped_column(nullable=True)
    G: Mapped[int] = mapped_column(nullable=True)
    A: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    PIM: Mapped[int] = mapped_column(nullable=True)
    TGF: Mapped[int] = mapped_column(nullable=True)
    TGA: Mapped[int] = mapped_column(nullable=True)
    EVG: Mapped[int] = mapped_column(nullable=True)
    PPG: Mapped[int] = mapped_column(nullable=True)
    SHG: Mapped[int] = mapped_column(nullable=True)
    OTG: Mapped[int] = mapped_column(nullable=True)
    first_g: Mapped[int] = mapped_column(nullable=True)
    GWG: Mapped[int] = mapped_column(nullable=True)
    GWG_Real: Mapped[int] = mapped_column(nullable=True)
    GWS: Mapped[int] = mapped_column(nullable=True)
    PS_Att: Mapped[int] = mapped_column(nullable=True)
    PS_G: Mapped[int] = mapped_column(nullable=True)
    PS_percent: Mapped[int] = mapped_column(nullable=True)
    with_G: Mapped[int] = mapped_column(nullable=True)
    without_G: Mapped[int] = mapped_column(nullable=True)
    G_GP: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)


class PlayerGoalsParamsFilteredMixin:
    G: Mapped[int] = mapped_column(nullable=True)
    A: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    EVG: Mapped[int] = mapped_column(nullable=True)
    PPG: Mapped[int] = mapped_column(nullable=True)
    SHG: Mapped[int] = mapped_column(nullable=True)
    OTG: Mapped[int] = mapped_column(nullable=True)
    first_g: Mapped[int] = mapped_column(nullable=True)
    GWG: Mapped[int] = mapped_column(nullable=True)
    GWG_Real: Mapped[int] = mapped_column(nullable=True)
    GWS: Mapped[int] = mapped_column(nullable=True)


class PlayerGoals(PlayerMetricMixin, PlayerGoalsParamsAllMixin, Base):
    __tablename__ = "pl_goals_api"



class PlayerGoalsFilter(PlayerMetricFilteredMixin, Base):
    __tablename__ = "pl_goals_api_filters"

    G: Mapped[int] = mapped_column(nullable=True)
    A: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    EVG: Mapped[int] = mapped_column(nullable=True)
    PPG: Mapped[int] = mapped_column(nullable=True)
    SHG: Mapped[int] = mapped_column(nullable=True)
    OTG: Mapped[int] = mapped_column(nullable=True)
    first_g: Mapped[int] = mapped_column(nullable=True)
    GWG: Mapped[int] = mapped_column(nullable=True)
    GWG_Real: Mapped[int] = mapped_column(nullable=True)
    GWS: Mapped[int] = mapped_column(nullable=True)


class PlayerPenalties(PlayerMetricMixin, Base):
    __tablename__ = "pl_penalties_api"

    PEN: Mapped[int] = mapped_column(nullable=True)
    PIM: Mapped[int] = mapped_column(nullable=True)
    Minor: Mapped[int] = mapped_column(nullable=True)
    Major: Mapped[int] = mapped_column(nullable=True)
    Misc: Mapped[int] = mapped_column(nullable=True)
    G_Misc: Mapped[int] = mapped_column(nullable=True)
    Match: Mapped[int] = mapped_column(nullable=True)
    PIM_G: Mapped[int] = mapped_column(nullable=True)
    PEN_Served: Mapped[int] = mapped_column(nullable=True)
    PEN_G: Mapped[int] = mapped_column(nullable=True)
    PIM_Others: Mapped[int] = mapped_column(nullable=True)
    PS_Att: Mapped[int] = mapped_column(nullable=True)


class PlayerPenaltiesFilter(PlayerMetricFilteredMixin, Base):
    __tablename__ = "pl_penalties_api_filters"

    PEN: Mapped[int] = mapped_column(nullable=True)
    PIM: Mapped[int] = mapped_column(nullable=True)
    Minor: Mapped[int] = mapped_column(nullable=True)
    Major: Mapped[int] = mapped_column(nullable=True)
    Misc: Mapped[int] = mapped_column(nullable=True)
    G_Misc: Mapped[int] = mapped_column(nullable=True)
    Match: Mapped[int] = mapped_column(nullable=True)
    PIM_G: Mapped[int] = mapped_column(nullable=True)
    PEN_Served: Mapped[int] = mapped_column(nullable=True)
    PEN_G: Mapped[int] = mapped_column(nullable=True)
    PIM_Others: Mapped[int] = mapped_column(nullable=True)
    PS_Att: Mapped[int] = mapped_column(nullable=True)

