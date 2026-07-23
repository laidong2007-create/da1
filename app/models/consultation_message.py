import uuid

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
if TYPE_CHECKING:
    from app.models.consultation_session import ConsultationSession


class ConsultationMessage(Base):
    """
    Model lưu từng tin nhắn trong một phiên hội thoại.
    """

    __tablename__ = "consultation_messages"

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

    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "consultation_sessions.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    # ==========================================
    # Message Information
    # ==========================================

    role: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    def __repr__(self) -> str:
        return (
            f"<ConsultationMessage(role='{self.role}')>"
        )

session: Mapped["ConsultationSession"] = relationship(
    back_populates="messages"
)