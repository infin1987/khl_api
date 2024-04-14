from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from db.api.config import Base


class ArenaMixin:
    idarena: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    arena: Mapped[str] = mapped_column(nullable=False)
    arena_en: Mapped[str] = mapped_column(nullable=False)
    arena_city: Mapped[str] = mapped_column(nullable=False)
    arena_city_en: Mapped[str] = mapped_column(nullable=False)
    tnt_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    tourname: Mapped[str] = mapped_column(nullable=False)
    season: Mapped[str] = mapped_column(nullable=False)
    league: Mapped[str] = mapped_column(nullable=False)
    tnt_type: Mapped[str] = mapped_column(nullable=False)
    capacity_total: Mapped[int] = mapped_column(nullable=True)
    audience_total: Mapped[int] = mapped_column(nullable=True)
    occupancy_rate: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                  nullable=True)
    max_ts: Mapped[int] = mapped_column(nullable=True)


class ArenaTnt(ArenaMixin, Base):

    __tablename__ = "arena_tnt_api"

    # idarena: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    # arena: Mapped[str] = mapped_column(nullable=False)
    # arena_en: Mapped[str] = mapped_column(nullable=False)
    # arena_city: Mapped[str] = mapped_column(nullable=False)
    # arena_city_en: Mapped[str] = mapped_column(nullable=False)
    # tnt_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    # tourname: Mapped[str] = mapped_column(nullable=False)
    # season: Mapped[str] = mapped_column(nullable=False)
    # league: Mapped[str] = mapped_column(nullable=False)
    # tnt_type: Mapped[str] = mapped_column(nullable=False)
    GP: Mapped[int] = mapped_column(nullable=False)
    SP: Mapped[int] = mapped_column(nullable=True)
    first_gamedate: Mapped[datetime] = mapped_column(nullable=False)
    # capacity_total: Mapped[int] = mapped_column(nullable=True)
    capacity_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                nullable=True)  # Исправить параметры под decimal(10,2)
    # audience_total: Mapped[int] = mapped_column(nullable=True)
    audience_avg: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
                                                nullable=True)  # Исправить параметры под decimal(10,2)
    # occupancy_rate: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True),
    #                                               nullable=True)
    max_audience: Mapped[int] = mapped_column(nullable=True)
    min_audience: Mapped[int] = mapped_column(nullable=True)
    hclubs: Mapped[int] = mapped_column(nullable=True)
    aclubs: Mapped[int] = mapped_column(nullable=True)
    # max_ts: Mapped[int] = mapped_column(nullable=True)


class ArenaGames(ArenaMixin, Base):

    __tablename__ = 'arena_games_api'

    # arena: Mapped[str] = mapped_column(nullable=False)
    # arena_en: Mapped[str] = mapped_column(nullable=False)
    # arena_city: Mapped[str] = mapped_column(nullable=False)
    # arena_city_en: Mapped[str] = mapped_column(nullable=False)
    # tnt_id: Mapped[int] = mapped_column(nullable=False)
    idseason: Mapped[int] = mapped_column(nullable=False)
    # tourname: Mapped[str] = mapped_column(nullable=False)
    # season: Mapped[str] = mapped_column(nullable=False)
    # league: Mapped[str] = mapped_column(nullable=False)
    # tnt_type: Mapped[str] = mapped_column(nullable=False)
    schedule_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    gamedate: Mapped[datetime] = mapped_column(nullable=False)
    # capacity_total: Mapped[int] = mapped_column(nullable=True)
    # audience_total: Mapped[int] = mapped_column(nullable=True)
    # occupancy_rate: Mapped[float] = mapped_column(Float(precision=5, decimal_return_scale=4, asdecimal=True), nullable=True)
    idclub_h: Mapped[int] = mapped_column(nullable=True)
    teamname_h: Mapped[str] = mapped_column(nullable=False)
    idclub_a: Mapped[int] = mapped_column(nullable=True)
    teamname_a: Mapped[str] = mapped_column(nullable=False)
    # max_ts: Mapped[int] = mapped_column(nullable=True)