from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column

from db.api.config import Base


class RefMixin:

    idref: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    position: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)
    birthdate: Mapped[str] = mapped_column(nullable=False)
    deathdate: Mapped[str] = mapped_column(nullable=False)
    tnt_id: Mapped[int] = mapped_column(nullable=False)
    idseason: Mapped[int] = mapped_column(nullable=False)
    tourname: Mapped[str] = mapped_column(nullable=False)
    season: Mapped[str] = mapped_column(nullable=False)
    league: Mapped[str] = mapped_column(nullable=False)
    tnt_type: Mapped[str] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    PIM: Mapped[int] = mapped_column(nullable=True)
    PIMA: Mapped[int] = mapped_column(nullable=True)
    PIMB: Mapped[int] = mapped_column(nullable=True)
    f2A: Mapped[int] = mapped_column(nullable=True)
    f2B: Mapped[int] = mapped_column(nullable=True)
    f2: Mapped[int] = mapped_column(nullable=True)
    f5A: Mapped[int] = mapped_column(nullable=True)
    f5B: Mapped[int] = mapped_column(nullable=True)
    f5: Mapped[int] = mapped_column(nullable=True)
    f25A: Mapped[int] = mapped_column(nullable=True)
    f25B: Mapped[int] = mapped_column(nullable=True)
    f25: Mapped[int] = mapped_column(nullable=True)
    f10A: Mapped[int] = mapped_column(nullable=True)
    f10B: Mapped[int] = mapped_column(nullable=True)
    f10: Mapped[int] = mapped_column(nullable=True)
    f20A: Mapped[int] = mapped_column(nullable=True)
    f20B: Mapped[int] = mapped_column(nullable=True)
    f20: Mapped[int] = mapped_column(nullable=True)
    fGkA: Mapped[int] = mapped_column(nullable=True)
    fGkB: Mapped[int] = mapped_column(nullable=True)
    fGk: Mapped[int] = mapped_column(nullable=True)
    psA: Mapped[int] = mapped_column(nullable=True)
    psB: Mapped[int] = mapped_column(nullable=True)
    ps: Mapped[int] = mapped_column(nullable=True)
    fTeamA: Mapped[int] = mapped_column(nullable=True)
    fTeamB: Mapped[int] = mapped_column(nullable=True)
    fTeam: Mapped[int] = mapped_column(nullable=True)
    PIM_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    PIMA_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    PIMB_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class RefTnt(RefMixin, Base):

    __tablename__ = "referee_tnt_api"


class RefGames(RefMixin, Base):

    __tablename__ = "referee_games_api"

    schedule_id: Mapped[int] = mapped_column(nullable=False)