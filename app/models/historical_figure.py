from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Text, DateTime, func, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.consultation_session import ConsultationSession

class HistoricalFigure(Base):
    __tablename__ = "historical_figures"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(150))
    era: Mapped[str] = mapped_column(String(100), index=True)
    avatar_url: Mapped[str] = mapped_column(String(255), nullable=True)
    persona_prompt: Mapped[str] = mapped_column(Text)
    bio: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    sessions: Mapped[List["ConsultationSession"]] = relationship("ConsultationSession", back_populates="historical_figure")