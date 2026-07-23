import uuid

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
if TYPE_CHECKING:
    from app.models.historical_figure import HistoricalFigure
    from app.models.document_source import DocumentSource
    from app.models.document_metadata import DocumentMetadata
    from app.models.document_chunk import DocumentChunk


class HistoricalDocument(Base):
    """
    Model lưu tài liệu lịch sử.
    """

    __tablename__ = "historical_documents"

    # ==========================================
    # Primary Key
    # ==========================================

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # ==========================================
    # Basic Information
    # ==========================================

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # ==========================================
    # Foreign Keys
    # ==========================================

    figure_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("historical_figures.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    source_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("document_sources.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )

    def __repr__(self) -> str:
        return (
            f"<HistoricalDocument("
            f"title='{self.title}')>"
        )


figure: Mapped["HistoricalFigure"] = relationship(
    back_populates="documents"
)

source: Mapped["DocumentSource"] = relationship(
    back_populates="documents"
)

metadata_info: Mapped["DocumentMetadata"] = relationship(
    back_populates="document",
    uselist=False,
    cascade="all, delete-orphan"
)

chunks: Mapped[list["DocumentChunk"]] = relationship(
    back_populates="document",
    cascade="all, delete-orphan"
)