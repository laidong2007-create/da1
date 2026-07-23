import uuid

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
if TYPE_CHECKING:
    from app.models.historical_document import HistoricalDocument


class DocumentSource(Base):
    """
    Model lưu thông tin nguồn tài liệu.
    """

    __tablename__ = "document_sources"

    # ==============================
    # Primary Key
    # ==============================

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # ==============================
    # Source Information
    # ==============================

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    author: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    publisher: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    published_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    def __repr__(self) -> str:
        return f"<DocumentSource(title='{self.title}')>"


documents: Mapped[list["HistoricalDocument"]] = relationship(
    back_populates="source"
)