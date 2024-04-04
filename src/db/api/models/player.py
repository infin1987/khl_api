from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
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
    __mapper_args__ = {'exclude_properties': ['team_status', 'net']}

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


class PlayersAssists(PlayersMetricMixin, Base):
    __tablename__ = "pl_assists_api"

    games_count: Mapped[int] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    G: Mapped[int] = mapped_column(nullable=True)
    A: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    EVA: Mapped[int] = mapped_column(nullable=True)
    PPA: Mapped[int] = mapped_column(nullable=True)
    SHA: Mapped[int] = mapped_column(nullable=True)
    A1: Mapped[int] = mapped_column(nullable=True)
    A2: Mapped[int] = mapped_column(nullable=True)
    with_A: Mapped[int] = mapped_column(nullable=True)
    without_A: Mapped[int] = mapped_column(nullable=True)
    A_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class PlayersAssistsFilter(PlayersMetricFilteredMixin, PlayersMetricMixin, Base):
    __tablename__ = "pl_assists_api_filters"

    games_count: Mapped[int] = mapped_column(nullable=False)
    G: Mapped[int] = mapped_column(nullable=True)
    A: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    EVA: Mapped[int] = mapped_column(nullable=True)
    PPA: Mapped[int] = mapped_column(nullable=True)
    SHA: Mapped[int] = mapped_column(nullable=True)
    A1: Mapped[int] = mapped_column(nullable=True)
    A2: Mapped[int] = mapped_column(nullable=True)


class PlayersPoints(PlayersMetricMixin, Base):
    __tablename__ = "pl_points_api"

    games_count: Mapped[int] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    G: Mapped[int] = mapped_column(nullable=True)
    A: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    pm: Mapped[int] = mapped_column(nullable=True)
    PIM: Mapped[int] = mapped_column(nullable=True)
    EVP: Mapped[int] = mapped_column(nullable=True)
    PPP: Mapped[int] = mapped_column(nullable=True)
    SHP: Mapped[int] = mapped_column(nullable=True)
    with_P: Mapped[int] = mapped_column(nullable=True)
    without_P: Mapped[int] = mapped_column(nullable=True)
    P_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)


class PlayersPointsFilter(PlayersMetricFilteredMixin, PlayersMetricMixin, Base):
    __tablename__ = "pl_points_api_filters"

    games_count: Mapped[int] = mapped_column(nullable=False)
    G: Mapped[int] = mapped_column(nullable=True)
    A: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    EVP: Mapped[int] = mapped_column(nullable=True)
    PPP: Mapped[int] = mapped_column(nullable=True)
    SHP: Mapped[int] = mapped_column(nullable=True)


class PlayersFaceoffs(PlayersMetricMixin, Base):
    __tablename__ = "pl_faceoffs_api"

    games_count: Mapped[int] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    G: Mapped[int] = mapped_column(nullable=True)
    A: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    pm: Mapped[int] = mapped_column(nullable=True)
    PIM: Mapped[int] = mapped_column(nullable=True)
    FO: Mapped[int] = mapped_column(nullable=True)
    FOW: Mapped[int] = mapped_column(nullable=True)
    FOL: Mapped[int] = mapped_column(nullable=True)
    FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    FOL_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    EV_FO: Mapped[int] = mapped_column(nullable=True)
    EV_FOW: Mapped[int] = mapped_column(nullable=True)
    EV_FOL: Mapped[int] = mapped_column(nullable=True)
    EV_FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    EV_FOL_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    PP_FO: Mapped[int] = mapped_column(nullable=True)
    PP_FOW: Mapped[int] = mapped_column(nullable=True)
    PP_FOL: Mapped[int] = mapped_column(nullable=True)
    PP_FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    PP_FOL_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    SH_FO: Mapped[int] = mapped_column(nullable=True)
    SH_FOW: Mapped[int] = mapped_column(nullable=True)
    SH_FOL: Mapped[int] = mapped_column(nullable=True)
    SH_FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    SH_FOL_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    FO_Ahd: Mapped[int] = mapped_column(nullable=True)
    FOW_Ahd: Mapped[int] = mapped_column(nullable=True)
    FO_Bhd: Mapped[int] = mapped_column(nullable=True)
    FOW_Bhd: Mapped[int] = mapped_column(nullable=True)
    FO_Close: Mapped[int] = mapped_column(nullable=True)
    FOW_Close: Mapped[int] = mapped_column(nullable=True)


class PlayersFaceoffsFilter(PlayersMetricFilteredMixin, PlayersMetricMixin, Base):
    __tablename__ = "pl_faceoffs_api_filters"
    __mapper_args__ = {'exclude_properties': ['net']}

    # net: Mapped[str] = mapped_column(nullable=True, deffered=True)
    games_count: Mapped[int] = mapped_column(nullable=False)
    FO: Mapped[int] = mapped_column(nullable=True)
    FOW: Mapped[int] = mapped_column(nullable=True)
    FOL: Mapped[int] = mapped_column(nullable=True)
    # FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    # FOL_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    EV_FO: Mapped[int] = mapped_column(nullable=True)
    EV_FOW: Mapped[int] = mapped_column(nullable=True)
    EV_FOL: Mapped[int] = mapped_column(nullable=True)
    # EV_FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    # EV_FOL_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    PP_FO: Mapped[int] = mapped_column(nullable=True)
    PP_FOW: Mapped[int] = mapped_column(nullable=True)
    PP_FOL: Mapped[int] = mapped_column(nullable=True)
    # PP_FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    # PP_FOL_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    SH_FO: Mapped[int] = mapped_column(nullable=True)
    SH_FOW: Mapped[int] = mapped_column(nullable=True)
    SH_FOL: Mapped[int] = mapped_column(nullable=True)
    # SH_FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    # SH_FOL_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    FO_Ahd: Mapped[int] = mapped_column(nullable=True)
    FOW_Ahd: Mapped[int] = mapped_column(nullable=True)
    FO_Bhd: Mapped[int] = mapped_column(nullable=True)
    FOW_Bhd: Mapped[int] = mapped_column(nullable=True)
    FO_Close: Mapped[int] = mapped_column(nullable=True)
    FOW_Close: Mapped[int] = mapped_column(nullable=True)


class PlayerActivity(PlayersMetricMixin, Base):
    __tablename__ = "pl_activity_api"

    games_count: Mapped[int] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    BkS: Mapped[int] = mapped_column(nullable=True)
    BkSA: Mapped[int] = mapped_column(nullable=True)
    EV_BkS: Mapped[int] = mapped_column(nullable=True)
    EV_BkSA: Mapped[int] = mapped_column(nullable=True)
    PP_BkS: Mapped[int] = mapped_column(nullable=True)
    PP_BkSA: Mapped[int] = mapped_column(nullable=True)
    SH_BkS: Mapped[int] = mapped_column(nullable=True)
    SH_BkSA: Mapped[int] = mapped_column(nullable=True)
    EN_BkS: Mapped[int] = mapped_column(nullable=True)
    EN_BkSA: Mapped[int] = mapped_column(nullable=True)
    ENO_BkS: Mapped[int] = mapped_column(nullable=True)
    ENO_BkSA: Mapped[int] = mapped_column(nullable=True)
    FoA: Mapped[int] = mapped_column(nullable=True)
    TkA: Mapped[int] = mapped_column(nullable=True)
    Hits: Mapped[int] = mapped_column(nullable=True)
    P_Intc: Mapped[int] = mapped_column(nullable=True)
    EV_Hits: Mapped[int] = mapped_column(nullable=True)
    EV_TkA: Mapped[int] = mapped_column(nullable=True)
    EV_P_Intc: Mapped[int] = mapped_column(nullable=True)
    EV_FoA: Mapped[int] = mapped_column(nullable=True)
    PP_Hits: Mapped[int] = mapped_column(nullable=True)
    PP_TkA: Mapped[int] = mapped_column(nullable=True)
    PP_P_Intc: Mapped[int] = mapped_column(nullable=True)
    PP_FoA: Mapped[int] = mapped_column(nullable=True)
    SH_Hits: Mapped[int] = mapped_column(nullable=True)
    SH_TkA: Mapped[int] = mapped_column(nullable=True)
    SH_P_Intc: Mapped[int] = mapped_column(nullable=True)
    SH_FoA: Mapped[int] = mapped_column(nullable=True)
    BkS_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    BkSA_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    Hits_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    TkA_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    P_Intc_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    FoA_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)


class PlayerActivityFilter(PlayersMetricFilteredMixin, PlayersMetricMixin, Base):
    __tablename__ = "pl_activity_api_filters"

    games_count: Mapped[int] = mapped_column(nullable=False)
    BkS: Mapped[int] = mapped_column(nullable=True)
    BkSA: Mapped[int] = mapped_column(nullable=True)
    EV_BkS: Mapped[int] = mapped_column(nullable=True)
    EV_BkSA: Mapped[int] = mapped_column(nullable=True)
    PP_BkS: Mapped[int] = mapped_column(nullable=True)
    PP_BkSA: Mapped[int] = mapped_column(nullable=True)
    SH_BkS: Mapped[int] = mapped_column(nullable=True)
    SH_BkSA: Mapped[int] = mapped_column(nullable=True)
    EN_BkS: Mapped[int] = mapped_column(nullable=True)
    EN_BkSA: Mapped[int] = mapped_column(nullable=True)
    ENO_BkS: Mapped[int] = mapped_column(nullable=True)
    ENO_BkSA: Mapped[int] = mapped_column(nullable=True)
    FoA: Mapped[int] = mapped_column(nullable=True)
    TkA: Mapped[int] = mapped_column(nullable=True)
    Hits: Mapped[int] = mapped_column(nullable=True)
    P_Intc: Mapped[int] = mapped_column(nullable=True)
    EV_Hits: Mapped[int] = mapped_column(nullable=True)
    EV_TkA: Mapped[int] = mapped_column(nullable=True)
    EV_P_Intc: Mapped[int] = mapped_column(nullable=True)
    EV_FoA: Mapped[int] = mapped_column(nullable=True)
    PP_Hits: Mapped[int] = mapped_column(nullable=True)
    PP_TkA: Mapped[int] = mapped_column(nullable=True)
    PP_P_Intc: Mapped[int] = mapped_column(nullable=True)
    PP_FoA: Mapped[int] = mapped_column(nullable=True)
    SH_Hits: Mapped[int] = mapped_column(nullable=True)
    SH_TkA: Mapped[int] = mapped_column(nullable=True)
    SH_P_Intc: Mapped[int] = mapped_column(nullable=True)
    SH_FoA: Mapped[int] = mapped_column(nullable=True)


class PlayerBullits(PlayersMetricMixin, Base):
    __tablename__ = "pl_bullits_api"

    games_count: Mapped[int] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    GWS: Mapped[int] = mapped_column(nullable=True)
    PS_Att: Mapped[int] = mapped_column(nullable=True)
    PS_G: Mapped[int] = mapped_column(nullable=True)
    PS_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    MiPS: Mapped[int] = mapped_column(nullable=True)
    BulS: Mapped[int] = mapped_column(nullable=True)
    BulG: Mapped[int] = mapped_column(nullable=True)
    BulS_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    Bul_Failed: Mapped[int] = mapped_column(nullable=True)
    Bul_Failed_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                  nullable=True)
    SOP: Mapped[int] = mapped_column(nullable=True)
    PS_SA: Mapped[int] = mapped_column(nullable=True)


class PlayerPlusminus(PlayersMetricMixin, Base):
    __tablename__ = "pl_plusminus_api"

    games_count: Mapped[int] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    G: Mapped[int] = mapped_column(nullable=True)
    A: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    pm: Mapped[int] = mapped_column(nullable=True)
    plus: Mapped[int] = mapped_column(nullable=True)
    minus: Mapped[int] = mapped_column(nullable=True)
    EV_TGF: Mapped[int] = mapped_column(nullable=True)
    EV_TGA: Mapped[int] = mapped_column(nullable=True)
    PP_TGF: Mapped[int] = mapped_column(nullable=True)
    PP_TGA: Mapped[int] = mapped_column(nullable=True)
    SH_TGF: Mapped[int] = mapped_column(nullable=True)
    SH_TGA: Mapped[int] = mapped_column(nullable=True)


class PlayerPlusminusFilter(PlayersMetricFilteredMixin, PlayersMetricMixin, Base):
    __tablename__ = "pl_plusminus_api_filters"
    __mapper_args__ = {'exclude_properties': ['team_status', 'net']}

    games_count: Mapped[int] = mapped_column(nullable=False)
    pm: Mapped[int] = mapped_column(nullable=True)
    plus: Mapped[int] = mapped_column(nullable=True)
    minus: Mapped[int] = mapped_column(nullable=True)
    EV_TGF: Mapped[int] = mapped_column(nullable=True)
    EV_TGA: Mapped[int] = mapped_column(nullable=True)
    PP_TGF: Mapped[int] = mapped_column(nullable=True)
    PP_TGA: Mapped[int] = mapped_column(nullable=True)
    SH_TGF: Mapped[int] = mapped_column(nullable=True)
    SH_TGA: Mapped[int] = mapped_column(nullable=True)


class PlayerToi(PlayersMetricMixin, Base):
    __tablename__ = "pl_toi_api"

    games_count: Mapped[int] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    EQ_TOI: Mapped[str] = mapped_column(nullable=False)
    PP_TOI: Mapped[str] = mapped_column(nullable=False)
    SH_TOI: Mapped[str] = mapped_column(nullable=False)
    EN_TOI: Mapped[str] = mapped_column(nullable=False)
    ENO_TOI: Mapped[str] = mapped_column(nullable=False)
    TOI: Mapped[str] = mapped_column(nullable=False)
    EQ_Sft: Mapped[int] = mapped_column(nullable=True)
    PP_Sft: Mapped[int] = mapped_column(nullable=True)
    SH_Sft: Mapped[int] = mapped_column(nullable=True)
    EN_Sft: Mapped[int] = mapped_column(nullable=True)
    ENO_Sft: Mapped[int] = mapped_column(nullable=True)
    Sft: Mapped[int] = mapped_column(nullable=True)
    PP_Times: Mapped[int] = mapped_column(nullable=True)
    SH_Times: Mapped[int] = mapped_column(nullable=True)
    EN_Times: Mapped[int] = mapped_column(nullable=True)
    ENO_Times: Mapped[int] = mapped_column(nullable=True)
    toi_avg: Mapped[str] = mapped_column(nullable=False)
    pptoi_avg: Mapped[str] = mapped_column(nullable=False)
    shtoi_avg: Mapped[str] = mapped_column(nullable=False)
    eqtoi_avg: Mapped[str] = mapped_column(nullable=False)
    entoi_avg: Mapped[str] = mapped_column(nullable=False)
    enotoi_avg: Mapped[str] = mapped_column(nullable=False)
    ppsft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    shsft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    eqsft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    ensft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    enosft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    sft_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)


class PlayerTOAD(PlayersMetricFilteredMixin, PlayersMetricMixin, Base):
    __tablename__ = "pl_toad_api"

    games_count: Mapped[int] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    ToO: Mapped[str] = mapped_column(nullable=False)
    EV_ToO: Mapped[str] = mapped_column(nullable=False)
    PP_ToO: Mapped[str] = mapped_column(nullable=False)
    SH_ToO: Mapped[str] = mapped_column(nullable=False)
    EN_ToO: Mapped[str] = mapped_column(nullable=False)
    ToD: Mapped[str] = mapped_column(nullable=False)
    EV_ToD: Mapped[str] = mapped_column(nullable=False)
    PP_ToD: Mapped[str] = mapped_column(nullable=False)
    SH_ToD: Mapped[str] = mapped_column(nullable=False)
    EN_ToD: Mapped[str] = mapped_column(nullable=False)
    ToO_avg: Mapped[str] = mapped_column(nullable=False)
    ToD_avg: Mapped[str] = mapped_column(nullable=False)


class PlayerShotAttempts(PlayersMetricMixin, Base):
    __tablename__ = "pl_shotattempts_api"

    games_count: Mapped[int] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    SAT_For: Mapped[int] = mapped_column(nullable=False)
    SAT_Against: Mapped[int] = mapped_column(nullable=False)
    SAT: Mapped[int] = mapped_column(nullable=False)
    SAT_Tied: Mapped[int] = mapped_column(nullable=False)
    SAT_Ahead: Mapped[int] = mapped_column(nullable=False)
    SAT_Behind: Mapped[int] = mapped_column(nullable=False)
    SAT_Close: Mapped[int] = mapped_column(nullable=False)
    USAT_For: Mapped[int] = mapped_column(nullable=False)
    USAT_Against: Mapped[int] = mapped_column(nullable=False)
    USAT: Mapped[int] = mapped_column(nullable=False)
    USAT_Tied: Mapped[int] = mapped_column(nullable=False)
    USAT_Ahead: Mapped[int] = mapped_column(nullable=False)
    USAT_Behind: Mapped[int] = mapped_column(nullable=False)
    USAT_Close: Mapped[int] = mapped_column(nullable=False)


class PlayerShotAttemptsFilter(PlayersMetricFilteredMixin, PlayersMetricMixin, Base):
    __tablename__ = "pl_shotattempts_api_filters"


    """
    фильтруем всегда по  PlayersMetricMixin, и обрjащение к filters \
    только по PlayersMetricFilteredMixin
    """

    games_count: Mapped[int] = mapped_column(nullable=False)
    SAT_For: Mapped[int] = mapped_column(nullable=False)
    SAT_Against: Mapped[int] = mapped_column(nullable=False)
    SAT: Mapped[int] = mapped_column(nullable=False)
    SAT_Tied: Mapped[int] = mapped_column(nullable=False)
    SAT_Ahead: Mapped[int] = mapped_column(nullable=False)
    SAT_Behind: Mapped[int] = mapped_column(nullable=False)
    SAT_Close: Mapped[int] = mapped_column(nullable=False)
    USAT_For: Mapped[int] = mapped_column(nullable=False)
    USAT_Against: Mapped[int] = mapped_column(nullable=False)
    USAT: Mapped[int] = mapped_column(nullable=False)
    USAT_Tied: Mapped[int] = mapped_column(nullable=False)
    USAT_Ahead: Mapped[int] = mapped_column(nullable=False)
    USAT_Behind: Mapped[int] = mapped_column(nullable=False)
    USAT_Close: Mapped[int] = mapped_column(nullable=False)


class PlayerSat(PlayersMetricMixin, Base):
    __tablename__ = "pl_sat_api"

    games_count: Mapped[int] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    SAT_percent: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                     asdecimal=True), nullable=True)
    SAT_Tied_percent: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                          asdecimal=True), nullable=True)
    SAT_Ahead_percent: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                           asdecimal=True), nullable=True)
    SAT_Behind_percent: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                            asdecimal=True), nullable=True)
    SAT_Close_percent: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                           asdecimal=True), nullable=True)
    USAT_percent: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                      asdecimal=True), nullable=True)
    USAT_Tied_percent: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                           asdecimal=True), nullable=True)
    USAT_Ahead_percent: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                            asdecimal=True), nullable=True)
    USAT_Behind_percent: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                             asdecimal=True), nullable=True)
    USAT_Close_percent: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                            asdecimal=True), nullable=True)
    SAT_G_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                   asdecimal=True), nullable=True)
    SAT_GSV_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4,
                                                     asdecimal=True), nullable=True)
