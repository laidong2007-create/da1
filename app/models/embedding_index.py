import uuid


from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
if TYPE_CHECKING:
    from app.models.document_chunk import DocumentChunk


class EmbeddingIndex(Base):
    """
    Model lưu thông tin Embedding của từng Chunk.
    """

    __tablename__ = "embedding_indexes"

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

    chunk_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "document_chunks.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        unique=True,
        index=True
    )

    # ==========================================
    # ChromaDB Information
    # ==========================================

    chroma_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    embedding_model: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    def __repr__(self) -> str:
        return (
            f"<EmbeddingIndex(chunk_id={self.chunk_id})>"
        )


chunk: Mapped["DocumentChunk"] = relationship(
    back_populates="embedding"
)