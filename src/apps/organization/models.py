from sqlalchemy import Integer, UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db.db_base import Base
from src.utils.func import get_random_uuid


class Organization(Base):
    __tablename__ = 'organization'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    phone: Mapped[int | None] = mapped_column(Integer)
    uuid: Mapped[UUID] = mapped_column(UUID, unique=True, default=get_random_uuid)
    email: Mapped[str | None] = mapped_column(String)
