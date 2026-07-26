from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, Text, DateTime, func, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.document_chunk import DocumentChunk
from app.models.document_metadata import DocumentMetadata
from app.models.document_source import DocumentSource

class HistoricalDocument(Base):
    __tablename__ = "historical_documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    content: Mapped[str] = mapped_column(Text)
    era: Mapped[Optional[str]] = mapped_column(String(100), index=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    chunks: Mapped[List["DocumentChunk"]] = relationship(
        "DocumentChunk", back_populates="document", cascade="all, delete-orphan"
    )
    metadata_list: Mapped[List["DocumentMetadata"]] = relationship(
        "DocumentMetadata", back_populates="document", cascade="all, delete-orphan"
    )
    sources: Mapped[List["DocumentSource"]] = relationship(
        "DocumentSource", back_populates="document", cascade="all, delete-orphan"
    )