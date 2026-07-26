from sqlalchemy import Integer, String, Text, ForeignKey  # <-- Phải có String ở đây
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    document_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("historical_documents.id", ondelete="CASCADE")
    )
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    vector_id: Mapped[str] = mapped_column(
        String(100), nullable=True
    )  # ID tương ứng trong ChromaDB

    # Relationship
    document = relationship("HistoricalDocument", back_populates="chunks")