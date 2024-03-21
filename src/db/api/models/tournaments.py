from sqlalchemy.orm import Mapped, mapped_column

from db.api.config import Base

class Tournaments(Base):
    __tablename__ = "tournaments_api"

    tnt_id: Mapped[int] = mapped_column(primary_key=True)
    level: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    nameen: Mapped[str] = mapped_column()
    season: Mapped[str] = mapped_column()
    startDate: Mapped[int] = mapped_column()
