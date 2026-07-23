import uuid

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
if TYPE_CHECKING:
    from app.models.historical_document import HistoricalDocument


class HistoricalFigure(Base):
    """
    Model lưu thông tin nhân vật lịch sử.
    """

    __tablename__ = "historical_figures"

    # ==========================
    # Primary Key
    # ==========================

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # ==========================
    # Basic Information
    # ==========================

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        index=True
    )

    birth_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    death_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    def __repr__(self):
        return f"<HistoricalFigure(name='{self.name}')>"


documents: Mapped[list["HistoricalDocument"]] = relationship(
    back_populates="figure",
    cascade="all, delete-orphan"
)