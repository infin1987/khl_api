from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from db.api.config import Base


class TrainerMixin:

    tnt_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    idseason: Mapped[int] = mapped_column(nullable=False)
    tourname: Mapped[str] = mapped_column(nullable=False)
    season: Mapped[str] = mapped_column(nullable=False)
    league: Mapped[str] = mapped_column(nullable=False)
    tnt_type: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    trainer_id: Mapped[int] = mapped_column(nullable=False)
    team_id: Mapped[int] = mapped_column(nullable=False)
    team_name: Mapped[str] = mapped_column(nullable=False)
    coach: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    birthdate: Mapped[str] = mapped_column(nullable=False)
    deathdate: Mapped[str] = mapped_column(nullable=False)

    W_Total: Mapped[int] = mapped_column(nullable=True)
    W0: Mapped[int] = mapped_column(nullable=True)
    W1: Mapped[int] = mapped_column(nullable=True)
    W2: Mapped[int] = mapped_column(nullable=True)
    W3: Mapped[int] = mapped_column(nullable=True)
    OTW: Mapped[int] = mapped_column(nullable=True)
    SOW: Mapped[int] = mapped_column(nullable=True)
    L_Total: Mapped[int] = mapped_column(nullable=True)
    L0: Mapped[int] = mapped_column(nullable=True)
    L1: Mapped[int] = mapped_column(nullable=True)
    L2: Mapped[int] = mapped_column(nullable=True)
    L3: Mapped[int] = mapped_column(nullable=True)
    SOL: Mapped[int] = mapped_column(nullable=True)
    OTL: Mapped[int] = mapped_column(nullable=True)
    T1: Mapped[int] = mapped_column(nullable=True)
    T2: Mapped[int] = mapped_column(nullable=True)
    T3: Mapped[int] = mapped_column(nullable=True)
    P: Mapped[int] = mapped_column(nullable=True)
    PP_Opp: Mapped[int] = mapped_column(nullable=True)
    PP_GF: Mapped[int] = mapped_column(nullable=True)
    SH_GF: Mapped[int] = mapped_column(nullable=True)
    PP_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    PP_GA: Mapped[int] = mapped_column(nullable=True)
    TS: Mapped[int] = mapped_column(nullable=True)
    SH_GA: Mapped[int] = mapped_column(nullable=True)
    PK_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)

    GtoS: Mapped[int] = mapped_column(nullable=True)
    GtoS_with_GF: Mapped[int] = mapped_column(nullable=True)
    GtoS_with_GF_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                    nullable=True)
    GtoS_without_GF: Mapped[int] = mapped_column(nullable=True)
    GtoS_without_GF_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                       nullable=True)
    GtoS_with_GA: Mapped[int] = mapped_column(nullable=True)
    GtoS_with_GA_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                    nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class TrainerTnt(TrainerMixin, Base):

    __tablename__ = "trainer_tnt_api"

    GP: Mapped[int] = mapped_column(nullable=False)
    W_pct: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)



class TrainerGames(TrainerMixin, Base):

    __tablename__ = "trainer_games_api"

    schedule_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    lt: Mapped[str] = mapped_column(nullable=False)

