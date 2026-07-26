from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class DocumentSource(Base):
    __tablename__ = "document_sources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    document_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("historical_documents.id", ondelete="CASCADE")
    )
    source_name: Mapped[str] = mapped_column(String(255), nullable=False)
    source_url: Mapped[str] = mapped_column(String(500), nullable=True)

    # Relationship (nếu có)
    document = relationship("HistoricalDocument", back_populates="sources")