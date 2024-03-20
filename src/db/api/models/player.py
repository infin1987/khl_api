from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column

from db.api.config import Base


class PlayersBioMixin:
    NAT: Mapped[str] = mapped_column(primary_key=True)
    S_NAT: Mapped[str] = mapped_column()
    birth_date: Mapped[int] = mapped_column()
    b_city: Mapped[str] = mapped_column()
    b_country: Mapped[str] = mapped_column()
    death_date: Mapped[int] = mapped_column()
    height: Mapped[int] = mapped_column()
    weight: Mapped[int] = mapped_column()
    status: Mapped[str] = mapped_column()


class PlayersMetricMixin:

    _to_sum = False
    global_id: Mapped[int] = mapped_column(primary_key=True)
    max_ts: Mapped[int] = mapped_column(primary_key=True)
    tnt_id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(primary_key=True)
    playername: Mapped[str] = mapped_column(primary_key=True)
    position: Mapped[str] = mapped_column()
    clid: Mapped[int] = mapped_column()
    team_name: Mapped[str] = mapped_column()
    season: Mapped[str] = mapped_column()
    league: Mapped[str] = mapped_column()
    tnt_type: Mapped[str] = mapped_column()


class PlayersMetricFilteredMixin:
    time_period: Mapped[int] = mapped_column(nullable=True)
    team_status: Mapped[str] = mapped_column(nullable=True)
    net: Mapped[str] = mapped_column(nullable=True)


class PlayersMainParamsMixin:
    GP: Mapped[int] = mapped_column(nullable=True)
    G: Mapped[int] = mapped_column(nullable=True)
    A: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    PIM: Mapped[int] = mapped_column(nullable=True)
    pm: Mapped[int] = mapped_column(nullable=True)


class PlayersBio(PlayersBioMixin, PlayersMetricMixin, PlayersMainParamsMixin, Base):
    __tablename__ = "pl_bio_api"


class PlayersGoals(PlayersMetricMixin, Base):
    __tablename__ = "pl_goals_api"

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


class PlayersGoalsFilter(PlayersMetricFilteredMixin, PlayersMetricMixin, Base):
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


class PlayersPenalties(PlayersMetricMixin, Base):
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


class PlayersPenaltiesFilter(PlayersMetricFilteredMixin, PlayersMetricMixin, Base):
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


class PlayersShots(PlayersMetricMixin, Base):
    __tablename__ = "pl_shots_api"

    G: Mapped[int] = mapped_column(primary_key=True)
    S: Mapped[int] = mapped_column(primary_key=True)
    SOG: Mapped[int] = mapped_column()
    MsS: Mapped[int] = mapped_column()
    EV_S: Mapped[int] = mapped_column()
    PP_S: Mapped[int] = mapped_column()
    SH_S: Mapped[int] = mapped_column()
    EN_S: Mapped[int] = mapped_column()
    ENO_S: Mapped[int] = mapped_column()
    EV_SOG: Mapped[int] = mapped_column()
    PP_SOG: Mapped[int] = mapped_column()
    SH_SOG: Mapped[int] = mapped_column()
    EN_SOG: Mapped[int] = mapped_column()
    ENO_SOG: Mapped[int] = mapped_column()
    EV_MsS: Mapped[int] = mapped_column()
    PP_MsS: Mapped[int] = mapped_column()
    SH_MsS: Mapped[int] = mapped_column()
    EN_MsS: Mapped[int] = mapped_column()
    ENO_MsS: Mapped[int] = mapped_column()
    G_GP: Mapped[int] = mapped_column()
    S_GP: Mapped[int] = mapped_column()
    SOG_GP: Mapped[int] = mapped_column()
    MsS_GP: Mapped[int] = mapped_column()


class PlayersShotsFilter(PlayersMetricFilteredMixin, PlayersMetricMixin, Base):
    __tablename__ = "pl_shots_api_filters"

    S: Mapped[int] = mapped_column(primary_key=True)
    SOG: Mapped[int] = mapped_column()
    MsS: Mapped[int] = mapped_column()
    EV_S: Mapped[int] = mapped_column()
    PP_S: Mapped[int] = mapped_column()
    SH_S: Mapped[int] = mapped_column()
    EN_S: Mapped[int] = mapped_column()
    ENO_S: Mapped[int] = mapped_column()
    EV_SOG: Mapped[int] = mapped_column()
    PP_SOG: Mapped[int] = mapped_column()
    SH_SOG: Mapped[int] = mapped_column()
    EN_SOG: Mapped[int] = mapped_column()
    ENO_SOG: Mapped[int] = mapped_column()
    EV_MsS: Mapped[int] = mapped_column()
    PP_MsS: Mapped[int] = mapped_column()
    SH_MsS: Mapped[int] = mapped_column()
    EN_MsS: Mapped[int] = mapped_column()
    ENO_MsS: Mapped[int] = mapped_column()


class PlayersTotal(PlayersMetricMixin, PlayersMainParamsMixin, Base):
    __tablename__ = "pl_total_api"

    EVG: Mapped[int] = mapped_column()
    PPG: Mapped[int] = mapped_column()
    SHG: Mapped[int] = mapped_column()
    OTG: Mapped[int] = mapped_column()
    first_g: Mapped[int] = mapped_column()
    GWG: Mapped[int] = mapped_column()
    GWS: Mapped[int] = mapped_column()
    plus: Mapped[int] = mapped_column()
    minus: Mapped[int] = mapped_column()
    toi_avg: Mapped[str] = mapped_column()
    pptoi_avg: Mapped[str] = mapped_column()
    shtoi_avg: Mapped[str] = mapped_column()
    eqtoi_avg: Mapped[str] = mapped_column()
    entoi_avg: Mapped[str] = mapped_column()
    ppsft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    shsft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    eqsft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    ensft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    sft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    FO: Mapped[int] = mapped_column()
    FOW: Mapped[int] = mapped_column()
    fo_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    FoA: Mapped[int] = mapped_column()
    TkA: Mapped[int] = mapped_column()
    Hits: Mapped[int] = mapped_column()
    P_Intc: Mapped[int] = mapped_column()
    S: Mapped[int] = mapped_column()
    SOG: Mapped[int] = mapped_column()
    sog_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    sog_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    toa_avg: Mapped[str] = mapped_column()

