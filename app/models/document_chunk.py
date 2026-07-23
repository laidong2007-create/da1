import uuid


from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
if TYPE_CHECKING:
    from app.models.historical_document import HistoricalDocument
    from app.models.embedding_index import EmbeddingIndex


class DocumentChunk(Base):
    """
    Model lưu từng đoạn (chunk) của tài liệu.
    """

    __tablename__ = "document_chunks"

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
        nullable=False,
        index=True
    )

    # ==========================================
    # Chunk Information
    # ==========================================

    chunk_index: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    def __repr__(self) -> str:
        return (
            f"<DocumentChunk("
            f"document_id={self.document_id}, "
            f"chunk_index={self.chunk_index})>"
        )


document: Mapped["HistoricalDocument"] = relationship(
    back_populates="chunks"
)

embedding: Mapped["EmbeddingIndex"] = relationship(
    back_populates="chunk",
    uselist=False,
    cascade="all, delete-orphan"
)