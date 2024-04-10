from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from db.api.config import Base


class TeamsMixin:
    club_name: Mapped[str] = mapped_column(nullable=False)
    clid: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    tnt_id: Mapped[int] = mapped_column(nullable=False)
    team_id: Mapped[int] = mapped_column(nullable=False)
    team_name: Mapped[str] = mapped_column(nullable=False)
    season: Mapped[str] = mapped_column(nullable=False)
    league: Mapped[str] = mapped_column(nullable=False)
    tnt_type: Mapped[str] = mapped_column(nullable=False)


class Teams_Tm6(TeamsMixin, Base):
    __tablename__ = "team_TM6_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    GF: Mapped[int] = mapped_column(nullable=False)
    GF_avg: Mapped[int] = mapped_column(nullable=False)
    GA: Mapped[int] = mapped_column(nullable=False)
    MsS: Mapped[int] = mapped_column(nullable=False)
    SF: Mapped[int] = mapped_column(nullable=False)
    SF_avg: Mapped[int] = mapped_column(nullable=False)
    SA: Mapped[int] = mapped_column(nullable=False)
    SA_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    SOG: Mapped[int] = mapped_column(nullable=False)
    SOGA: Mapped[int] = mapped_column(nullable=False)
    S_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    SOG_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    BkS: Mapped[int] = mapped_column(nullable=False)
    BkSA: Mapped[int] = mapped_column(nullable=False)
    PP_S: Mapped[int] = mapped_column(nullable=False)
    PP_SOG: Mapped[int] = mapped_column(nullable=False)
    PP_MsS: Mapped[int] = mapped_column(nullable=False)
    PP_BkS: Mapped[int] = mapped_column(nullable=False)
    PP_BkSA: Mapped[int] = mapped_column(nullable=False)
    SH_S: Mapped[int] = mapped_column(nullable=False)
    SH_SOG: Mapped[int] = mapped_column(nullable=False)
    SH_MsS: Mapped[int] = mapped_column(nullable=False)
    SH_BkS: Mapped[int] = mapped_column(nullable=False)
    SH_BkSA: Mapped[int] = mapped_column(nullable=False)
    EV_S: Mapped[int] = mapped_column(nullable=False)
    EV_SOG: Mapped[int] = mapped_column(nullable=False)
    EV_MsS: Mapped[int] = mapped_column(nullable=False)
    EV_BkS: Mapped[int] = mapped_column(nullable=False)
    EV_BkSA: Mapped[int] = mapped_column(nullable=False)
    SOG_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    MsS_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    BulS: Mapped[int] = mapped_column(nullable=False)
    Bul_SA: Mapped[int] = mapped_column(nullable=False)
    BulG: Mapped[int] = mapped_column(nullable=False)
    Bul_Failed: Mapped[int] = mapped_column(nullable=False)
    Bul_Saves: Mapped[int] = mapped_column(nullable=False)
    max_ts: Mapped[int] = mapped_column(nullable=False)


class Teams_Tm11(TeamsMixin, Base):
    __tablename__ = "team_TM11_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    GP_A: Mapped[int] = mapped_column(nullable=False)
    GP_B: Mapped[int] = mapped_column(nullable=False)
    W_1G: Mapped[int] = mapped_column(nullable=False)
    L_1G: Mapped[int] = mapped_column(nullable=False)
    W_3G: Mapped[int] = mapped_column(nullable=False)
    L_3G: Mapped[int] = mapped_column(nullable=False)
    OTL_1G: Mapped[int] = mapped_column(nullable=False)
    W_Score1: Mapped[int] = mapped_column(nullable=False)
    L_Score1: Mapped[int] = mapped_column(nullable=False)
    OTW_Score1: Mapped[int] = mapped_column(nullable=False)
    OTL_Score1: Mapped[int] = mapped_column(nullable=False)
    W_Score1_Opp: Mapped[int] = mapped_column(nullable=False)
    L_Score1_Opp: Mapped[int] = mapped_column(nullable=False)
    OTW_Score1_Opp: Mapped[int] = mapped_column(nullable=False)
    OTL_Score1_Opp: Mapped[int] = mapped_column(nullable=False)
    score1: Mapped[int] = mapped_column(nullable=False)
    score1_opp: Mapped[int] = mapped_column(nullable=False)
    W_Total: Mapped[int] = mapped_column(nullable=False)
    W1: Mapped[int] = mapped_column(nullable=False)
    W2: Mapped[int] = mapped_column(nullable=False)
    W3: Mapped[int] = mapped_column(nullable=False)
    OTW: Mapped[int] = mapped_column(nullable=False)
    SOW: Mapped[int] = mapped_column(nullable=False)
    W0: Mapped[int] = mapped_column(nullable=False)
    W: Mapped[int] = mapped_column(nullable=False)
    L_Total: Mapped[int] = mapped_column(nullable=False)
    L1: Mapped[int] = mapped_column(nullable=False)
    L2: Mapped[int] = mapped_column(nullable=False)
    L3: Mapped[int] = mapped_column(nullable=False)
    T1: Mapped[int] = mapped_column(nullable=False)
    T2: Mapped[int] = mapped_column(nullable=False)
    T3: Mapped[int] = mapped_column(nullable=False)
    SOL: Mapped[int] = mapped_column(nullable=False)
    OTL: Mapped[int] = mapped_column(nullable=False)
    L0: Mapped[int] = mapped_column(nullable=False)
    L: Mapped[int] = mapped_column(nullable=False)
    W_total_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    W0_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    OTW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    SOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    W_1G_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    W_3G_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm14(TeamsMixin, Base):
    __tablename__ = "team_TM14_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    SOA: Mapped[int] = mapped_column(nullable=False)
    SO: Mapped[int] = mapped_column(nullable=False)
    GF: Mapped[int] = mapped_column(nullable=False)
    GA: Mapped[int] = mapped_column(nullable=False)
    GWS: Mapped[int] = mapped_column(nullable=False)
    GWS_A: Mapped[int] = mapped_column(nullable=False)
    EV_GF: Mapped[int] = mapped_column(nullable=False)
    PP_GF: Mapped[int] = mapped_column(nullable=False)
    SH_GF: Mapped[int] = mapped_column(nullable=False)
    GF1: Mapped[int] = mapped_column(nullable=False)
    GF2: Mapped[int] = mapped_column(nullable=False)
    GF3: Mapped[int] = mapped_column(nullable=False)
    GF_OT: Mapped[int] = mapped_column(nullable=False)
    EV_GA: Mapped[int] = mapped_column(nullable=False)
    PP_GA: Mapped[int] = mapped_column(nullable=False)
    SH_GA: Mapped[int] = mapped_column(nullable=False)
    GA1: Mapped[int] = mapped_column(nullable=False)
    GA2: Mapped[int] = mapped_column(nullable=False)
    GA3: Mapped[int] = mapped_column(nullable=False)
    GA_OT: Mapped[int] = mapped_column(nullable=False)
    EN_GF: Mapped[int] = mapped_column(nullable=False)
    EN_GA: Mapped[int] = mapped_column(nullable=False)
    first_gf: Mapped[int] = mapped_column(nullable=False)
    first_ga: Mapped[int] = mapped_column(nullable=False)
    GF_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    GA_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=False)


class Teams_Tm5(TeamsMixin, Base):
    __tablename__ = "team_TM5_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    PIM: Mapped[int] = mapped_column(nullable=False)
    PIM_Opp: Mapped[int] = mapped_column(nullable=False)
    PEN: Mapped[int] = mapped_column(nullable=False)
    minor: Mapped[int] = mapped_column(nullable=False)
    major: Mapped[int] = mapped_column(nullable=False)
    Match: Mapped[int] = mapped_column(nullable=False)
    Misc: Mapped[int] = mapped_column(nullable=False)
    G_Misc: Mapped[int] = mapped_column(nullable=False)
    PIM_G: Mapped[int] = mapped_column(nullable=False)
    PS_Att: Mapped[int] = mapped_column(nullable=False)
    PS_GA: Mapped[int] = mapped_column(nullable=False)
    Bench: Mapped[int] = mapped_column(nullable=False)
    PIM_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=False)


class Teams_Tm7(TeamsMixin, Base):
    __tablename__ = "team_TM7_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    FO: Mapped[int] = mapped_column(nullable=False)
    FOW: Mapped[int] = mapped_column(nullable=False)
    FOL: Mapped[int] = mapped_column(nullable=False)
    EV_FO: Mapped[int] = mapped_column(nullable=False)
    EV_FOW: Mapped[int] = mapped_column(nullable=False)
    PP_FO: Mapped[int] = mapped_column(nullable=False)
    PP_FOW: Mapped[int] = mapped_column(nullable=False)
    SH_FO: Mapped[int] = mapped_column(nullable=False)
    SH_FOW: Mapped[int] = mapped_column(nullable=False)
    FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    EV_FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    PP_FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    SH_FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=False)


class Teams_Tm20(TeamsMixin, Base):
    __tablename__ = "team_TM20_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    FO: Mapped[int] = mapped_column(nullable=False)
    FOW: Mapped[int] = mapped_column(nullable=False)
    FO_Ahd: Mapped[int] = mapped_column(nullable=False)
    FOW_Ahd: Mapped[int] = mapped_column(nullable=False)
    FO_Bhd: Mapped[int] = mapped_column(nullable=False)
    FOW_Bhd: Mapped[int] = mapped_column(nullable=False)
    FO_Close: Mapped[int] = mapped_column(nullable=False)
    FOW_Close: Mapped[int] = mapped_column(nullable=False)
    FOW_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=False)


class Teams_Tm22(TeamsMixin, Base):
    __tablename__ = "team_TM22_api"

    GP: Mapped[int] = mapped_column(nullable=False)
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
    Hits_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    TkA_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    P_Intc_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    FoA_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm8(TeamsMixin, Base):
    __tablename__ = "team_TM8_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    SOP: Mapped[int] = mapped_column(nullable=True)
    GWS: Mapped[int] = mapped_column(nullable=True)
    GWS_A: Mapped[int] = mapped_column(nullable=True)
    BulS: Mapped[int] = mapped_column(nullable=True)
    Bul_SA: Mapped[int] = mapped_column(nullable=True)
    BulG: Mapped[int] = mapped_column(nullable=True)
    Bul_GA: Mapped[int] = mapped_column(nullable=True)
    BulS_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    Bul_Saves: Mapped[int] = mapped_column(nullable=True)
    BulSv_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    PS_Att: Mapped[int] = mapped_column(nullable=True)
    PS_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm12(TeamsMixin, Base):
    __tablename__ = "team_TM12_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    GF: Mapped[int] = mapped_column(nullable=True)
    GA: Mapped[int] = mapped_column(nullable=True)
    GF_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    GA_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    GF55: Mapped[int] = mapped_column(nullable=True)
    GF54: Mapped[int] = mapped_column(nullable=True)
    GF53: Mapped[int] = mapped_column(nullable=True)
    GF56: Mapped[int] = mapped_column(nullable=True)
    GF46: Mapped[int] = mapped_column(nullable=True)
    GF45: Mapped[int] = mapped_column(nullable=True)
    GF44: Mapped[int] = mapped_column(nullable=True)
    GF43: Mapped[int] = mapped_column(nullable=True)
    GF36: Mapped[int] = mapped_column(nullable=True)
    GF35: Mapped[int] = mapped_column(nullable=True)
    GF34: Mapped[int] = mapped_column(nullable=True)
    GF33: Mapped[int] = mapped_column(nullable=True)
    GF65: Mapped[int] = mapped_column(nullable=True)
    GF64: Mapped[int] = mapped_column(nullable=True)
    GF63: Mapped[int] = mapped_column(nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm13(TeamsMixin, Base):
    __tablename__ = "team_TM13_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    GF: Mapped[int] = mapped_column(nullable=True)
    GA: Mapped[int] = mapped_column(nullable=True)
    GF_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    GA_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    GA55: Mapped[int] = mapped_column(nullable=True)
    GA54: Mapped[int] = mapped_column(nullable=True)
    GA53: Mapped[int] = mapped_column(nullable=True)
    GA56: Mapped[int] = mapped_column(nullable=True)
    GA46: Mapped[int] = mapped_column(nullable=True)
    GA45: Mapped[int] = mapped_column(nullable=True)
    GA44: Mapped[int] = mapped_column(nullable=True)
    GA43: Mapped[int] = mapped_column(nullable=True)
    GA36: Mapped[int] = mapped_column(nullable=True)
    GA35: Mapped[int] = mapped_column(nullable=True)
    GA34: Mapped[int] = mapped_column(nullable=True)
    GA33: Mapped[int] = mapped_column(nullable=True)
    GA65: Mapped[int] = mapped_column(nullable=True)
    GA64: Mapped[int] = mapped_column(nullable=True)
    GA63: Mapped[int] = mapped_column(nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm9(TeamsMixin, Base):
    __tablename__ = "team_TM9_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    W_Total: Mapped[int] = mapped_column(nullable=True)
    W1: Mapped[int] = mapped_column(nullable=True)
    W2: Mapped[int] = mapped_column(nullable=True)
    W3: Mapped[int] = mapped_column(nullable=True)
    OTW: Mapped[int] = mapped_column(nullable=True)
    SOW: Mapped[int] = mapped_column(nullable=True)
    W0: Mapped[int] = mapped_column(nullable=True)
    L_Total: Mapped[int] = mapped_column(nullable=True)
    L1: Mapped[int] = mapped_column(nullable=True)
    L2: Mapped[int] = mapped_column(nullable=True)
    L3: Mapped[int] = mapped_column(nullable=True)
    SOL: Mapped[int] = mapped_column(nullable=True)
    OTL: Mapped[int] = mapped_column(nullable=True)
    L0: Mapped[int] = mapped_column(nullable=True)
    T1: Mapped[int] = mapped_column(nullable=True)
    T2: Mapped[int] = mapped_column(nullable=True)
    T3: Mapped[int] = mapped_column(nullable=True)
    W_L1P: Mapped[int] = mapped_column(nullable=True)
    L_L1P: Mapped[int] = mapped_column(nullable=True)
    OTW_L1P: Mapped[int] = mapped_column(nullable=True)
    OTL_L1P: Mapped[int] = mapped_column(nullable=True)
    W_L1P_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    W_L2P: Mapped[int] = mapped_column(nullable=True)
    L_L2P: Mapped[int] = mapped_column(nullable=True)
    OTW_L2P: Mapped[int] = mapped_column(nullable=True)
    OTL_L2P: Mapped[int] = mapped_column(nullable=True)
    W_L2P_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    W_T1P: Mapped[int] = mapped_column(nullable=True)
    L_T1P: Mapped[int] = mapped_column(nullable=True)
    OTW_T1P: Mapped[int] = mapped_column(nullable=True)
    OTL_T1P: Mapped[int] = mapped_column(nullable=True)
    W_T1P_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    W_T2P: Mapped[int] = mapped_column(nullable=True)
    L_T2P: Mapped[int] = mapped_column(nullable=True)
    OTW_T2P: Mapped[int] = mapped_column(nullable=True)
    OTL_T2P: Mapped[int] = mapped_column(nullable=True)
    W_T2P_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm17(TeamsMixin, Base):
    __tablename__ = "team_TM17_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    W_Total: Mapped[int] = mapped_column(nullable=True)
    W1: Mapped[int] = mapped_column(nullable=True)
    W2: Mapped[int] = mapped_column(nullable=True)
    W3: Mapped[int] = mapped_column(nullable=True)
    OTW: Mapped[int] = mapped_column(nullable=True)
    SOW: Mapped[int] = mapped_column(nullable=True)
    W0: Mapped[int] = mapped_column(nullable=True)
    L_Total: Mapped[int] = mapped_column(nullable=True)
    L1: Mapped[int] = mapped_column(nullable=True)
    L2: Mapped[int] = mapped_column(nullable=True)
    L3: Mapped[int] = mapped_column(nullable=True)
    SOL: Mapped[int] = mapped_column(nullable=True)
    OTL: Mapped[int] = mapped_column(nullable=True)
    L0: Mapped[int] = mapped_column(nullable=True)
    W_Score1: Mapped[int] = mapped_column(nullable=True)
    L_Score1: Mapped[int] = mapped_column(nullable=True)
    OTW_Score1: Mapped[int] = mapped_column(nullable=True)
    OTL_Score1: Mapped[int] = mapped_column(nullable=True)
    W_Score1_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                nullable=True)
    W_Score1_Opp: Mapped[int] = mapped_column(nullable=True)
    L_Score1_Opp: Mapped[int] = mapped_column(nullable=True)
    OTW_Score1_Opp: Mapped[int] = mapped_column(nullable=True)
    OTL_Score1_Opp: Mapped[int] = mapped_column(nullable=True)
    W_Score1_Opp_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                    nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm10(TeamsMixin, Base):
    __tablename__ = "team_TM10_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    S_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    SA_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    W_OutS: Mapped[int] = mapped_column(nullable=True)
    L_OutS: Mapped[int] = mapped_column(nullable=True)
    OTW_OutS: Mapped[int] = mapped_column(nullable=True)
    OTL_OutS: Mapped[int] = mapped_column(nullable=True)
    W_OutS_Opp: Mapped[int] = mapped_column(nullable=True)
    L_OutS_Opp: Mapped[int] = mapped_column(nullable=True)
    OTW_OutS_Opp: Mapped[int] = mapped_column(nullable=True)
    OTL_OutS_Opp: Mapped[int] = mapped_column(nullable=True)
    W_EvenS: Mapped[int] = mapped_column(nullable=True)
    L_EvenS: Mapped[int] = mapped_column(nullable=True)
    OTW_EvenS: Mapped[int] = mapped_column(nullable=True)
    OTL_EvenS: Mapped[int] = mapped_column(nullable=True)
    score1: Mapped[int] = mapped_column(nullable=True)
    score1_opp: Mapped[int] = mapped_column(nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm15(TeamsMixin, Base):
    __tablename__ = "team_TM15_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    PP_Opp: Mapped[int] = mapped_column(nullable=True)
    PP_Time: Mapped[str] = mapped_column(nullable=True)
    PK_Time: Mapped[str] = mapped_column(nullable=True)
    PP_PK_Time: Mapped[str] = mapped_column(nullable=True)
    P1_PP: Mapped[int] = mapped_column(nullable=True)
    P2_PP: Mapped[int] = mapped_column(nullable=True)
    P3_PP: Mapped[int] = mapped_column(nullable=True)
    OT_PP: Mapped[int] = mapped_column(nullable=True)
    s54_Time: Mapped[str] = mapped_column(nullable=True)
    s54_Opp: Mapped[int] = mapped_column(nullable=True)
    s53_Time: Mapped[str] = mapped_column(nullable=True)
    s53_Opp: Mapped[int] = mapped_column(nullable=True)
    s43_Time: Mapped[str] = mapped_column(nullable=True)
    s43_Opp: Mapped[int] = mapped_column(nullable=True)
    P1_PP_Time: Mapped[str] = mapped_column(nullable=True)
    P1_Diff: Mapped[str] = mapped_column(nullable=True)
    P2_PP_Time: Mapped[str] = mapped_column(nullable=True)
    P2_Diff: Mapped[str] = mapped_column(nullable=True)
    P3_PP_Time: Mapped[str] = mapped_column(nullable=True)
    P3_Diff: Mapped[str] = mapped_column(nullable=True)
    OT_PP_Time: Mapped[str] = mapped_column(nullable=True)
    OT_Diff: Mapped[str] = mapped_column(nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm16(TeamsMixin, Base):
    __tablename__ = "team_TM16_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    TS: Mapped[int] = mapped_column(nullable=True)
    PP_Time: Mapped[str] = mapped_column(nullable=True)
    PK_Time: Mapped[str] = mapped_column(nullable=True)
    PP_PK_Time: Mapped[str] = mapped_column(nullable=True)
    P1_SH: Mapped[int] = mapped_column(nullable=True)
    P2_SH: Mapped[int] = mapped_column(nullable=True)
    P3_SH: Mapped[int] = mapped_column(nullable=True)
    OT_SH: Mapped[int] = mapped_column(nullable=True)
    s45_Time: Mapped[str] = mapped_column(nullable=True)
    s45_Opp: Mapped[int] = mapped_column(nullable=True)
    s35_Time: Mapped[str] = mapped_column(nullable=True)
    s35_Opp: Mapped[int] = mapped_column(nullable=True)
    s34_Time: Mapped[str] = mapped_column(nullable=True)
    s34_Opp: Mapped[int] = mapped_column(nullable=True)
    P1_PK_Time: Mapped[str] = mapped_column(nullable=True)
    P1_Diff: Mapped[str] = mapped_column(nullable=True)
    P2_PK_Time: Mapped[str] = mapped_column(nullable=True)
    P2_Diff: Mapped[str] = mapped_column(nullable=True)
    P3_PK_Time: Mapped[str] = mapped_column(nullable=True)
    P3_Diff: Mapped[str] = mapped_column(nullable=True)
    OT_PK_Time: Mapped[str] = mapped_column(nullable=True)
    OT_Diff: Mapped[str] = mapped_column(nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm18(TeamsMixin, Base):
    __tablename__ = "team_TM18_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    SAT_For: Mapped[int] = mapped_column(nullable=True)
    SAT_Against: Mapped[int] = mapped_column(nullable=True)
    SAT: Mapped[int] = mapped_column(nullable=True)
    SAT_Rel_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                               nullable=True)
    SAT_Tied: Mapped[int] = mapped_column(nullable=True)
    SAT_Ahead: Mapped[int] = mapped_column(nullable=True)
    SAT_Behind: Mapped[int] = mapped_column(nullable=True)
    SAT_Close: Mapped[int] = mapped_column(nullable=True)
    USAT_For: Mapped[int] = mapped_column(nullable=True)
    USAT_Against: Mapped[int] = mapped_column(nullable=True)
    USAT: Mapped[int] = mapped_column(nullable=True)
    USAT_Rel_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                nullable=True)
    USAT_Tied: Mapped[int] = mapped_column(nullable=True)
    USAT_Ahead: Mapped[int] = mapped_column(nullable=True)
    USAT_Behind: Mapped[int] = mapped_column(nullable=True)
    USAT_Close: Mapped[int] = mapped_column(nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm19(TeamsMixin, Base):
    __tablename__ = "team_TM19_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    SAT_For: Mapped[int] = mapped_column(nullable=True)
    SAT_Against: Mapped[int] = mapped_column(nullable=True)
    SAT: Mapped[int] = mapped_column(nullable=True)
    SAT_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    SAT_Tied_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                nullable=True)
    SAT_Ahead_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                 nullable=True)
    SAT_Behind_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                  nullable=True)
    SAT_Close_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                 nullable=True)
    USAT_For: Mapped[int] = mapped_column(nullable=True)
    USAT_Against: Mapped[int] = mapped_column(nullable=True)
    USAT: Mapped[int] = mapped_column(nullable=True)
    USAT_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    USAT_Tied_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                 nullable=True)
    USAT_Ahead_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                  nullable=True)
    USAT_Behind_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                   nullable=True)
    USAT_Close_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                  nullable=True)
    S_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    Sv_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    SPSv_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm21(TeamsMixin, Base):
    __tablename__ = "team_TM21_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    ToA: Mapped[str] = mapped_column(nullable=True)
    ToD: Mapped[str] = mapped_column(nullable=True)
    PP_ToA: Mapped[str] = mapped_column(nullable=True)
    SH_ToA: Mapped[str] = mapped_column(nullable=True)
    EV_ToA: Mapped[str] = mapped_column(nullable=True)
    PP_ToD: Mapped[str] = mapped_column(nullable=True)
    SH_ToD: Mapped[str] = mapped_column(nullable=True)
    EV_ToD: Mapped[str] = mapped_column(nullable=True)
    ToD_Extra: Mapped[str] = mapped_column(nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm25(TeamsMixin, Base):
    __tablename__ = "team_TM25_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    W_Total: Mapped[int] = mapped_column(nullable=False)
    L_Total: Mapped[int] = mapped_column(nullable=False)
    h_arenas_total: Mapped[int] = mapped_column(nullable=False)
    h_arena_capacity_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                        nullable=True)
    h_arena_audience: Mapped[int] = mapped_column(nullable=False)
    h_arena_audience_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                        nullable=True)
    h_occupancy_rate: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                    nullable=True)
    r_arenas_total: Mapped[int] = mapped_column(nullable=False)
    r_arena_capacity_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                        nullable=True)
    r_arena_audience: Mapped[int] = mapped_column(nullable=False)
    r_arena_audience_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                        nullable=True)
    r_occupancy_rate: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                    nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class Teams_Tm1(TeamsMixin, Base):
    __tablename__ = "team_TM1_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    W_Total: Mapped[int] = mapped_column(nullable=True)
    W1: Mapped[int] = mapped_column(nullable=True)
    W2: Mapped[int] = mapped_column(nullable=True)
    W3: Mapped[int] = mapped_column(nullable=True)
    OTW: Mapped[int] = mapped_column(nullable=True)
    SOW: Mapped[int] = mapped_column(nullable=True)
    W0: Mapped[int] = mapped_column(nullable=True)
    L_Total: Mapped[int] = mapped_column(nullable=True)
    L1: Mapped[int] = mapped_column(nullable=True)
    L2: Mapped[int] = mapped_column(nullable=True)
    L3: Mapped[int] = mapped_column(nullable=True)
    SOL: Mapped[int] = mapped_column(nullable=True)
    OTL: Mapped[int] = mapped_column(nullable=True)
    L0: Mapped[int] = mapped_column(nullable=True)
    T1: Mapped[int] = mapped_column(nullable=True)
    T2: Mapped[int] = mapped_column(nullable=True)
    T3: Mapped[int] = mapped_column(nullable=True)
    PIM: Mapped[int] = mapped_column(nullable=True)
    PIMA: Mapped[int] = mapped_column(nullable=True)
    GF: Mapped[int] = mapped_column(nullable=True)
    GA: Mapped[int] = mapped_column(nullable=True)
    GF_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    GA_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    PP_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    PK_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    h_arena_capacity_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                        nullable=True)
    h_arena_audience_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                        nullable=True)
    h_occupancy_rate: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                    nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)

