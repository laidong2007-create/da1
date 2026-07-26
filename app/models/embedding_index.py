from datetime import datetime
from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class EmbeddingIndex(Base):
    __tablename__ = "embedding_indexes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    collection_name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    total_vectors: Mapped[int] = mapped_column(Integer, default=0)
    last_synced_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())