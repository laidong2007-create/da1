from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Text, String, DateTime, func, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.models.consultation_session import ConsultationSession

class ConsultationMessage(Base):
    __tablename__ = "consultation_messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("consultation_sessions.id"))
    sender: Mapped[str] = mapped_column(String(20)) # 'user' hoặc 'assistant'
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    session: Mapped["ConsultationSession"] = relationship("ConsultationSession", back_populates="messages")