import uuid

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.historical_document import HistoricalDocument


class DocumentMetadata(Base):
    """
    Model lưu metadata của tài liệu.
    """

    __tablename__ = "document_metadata"

    # ==========================================
    # Primary Key
    # ==========================================

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # ==========================================
    # Foreign Key
    # ==========================================

    document_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "historical_documents.id",
            ondelete="CASCADE"
        ),
        unique=True,
        nullable=False,
        index=True
    )

    # ==========================================
    # Metadata
    # ==========================================

    language: Mapped[str] = mapped_column(
        String(20),
        default="vi",
        nullable=False
    )

    keywords: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    def __repr__(self) -> str:
        return (
            f"<DocumentMetadata(document_id={self.document_id})>"
        )


document: Mapped["HistoricalDocument"] = relationship(
    back_populates="metadata_info"
)