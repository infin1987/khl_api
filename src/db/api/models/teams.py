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

