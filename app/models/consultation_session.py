from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import String, DateTime, func, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.historical_figure import HistoricalFigure
    from app.models.consultation_message import ConsultationMessage

class ConsultationSession(Base):
    __tablename__ = "consultation_sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    figure_id: Mapped[int] = mapped_column(ForeignKey("historical_figures.id"))
    title: Mapped[str] = mapped_column(String(200), default="Cuộc trò chuyện mới")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["User"] = relationship("User", back_populates="sessions")
    historical_figure: Mapped["HistoricalFigure"] = relationship("HistoricalFigure", back_populates="sessions")
    messages: Mapped[List["ConsultationMessage"]] = relationship("ConsultationMessage", back_populates="session", cascade="all, delete-orphan")