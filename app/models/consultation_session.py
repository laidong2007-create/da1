import uuid

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.consultation_message import ConsultationMessage



class ConsultationSession(Base):
    """
    Model lưu phiên hội thoại với AI.
    """

    __tablename__ = "consultation_sessions"

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

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    # ==========================================
    # Session Information
    # ==========================================

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    def __repr__(self) -> str:
        return (
            f"<ConsultationSession(title='{self.title}')>"
        )


user: Mapped["User"] = relationship(
    back_populates="consultation_sessions"
)

messages: Mapped[list["ConsultationMessage"]] = relationship(
    back_populates="session",
    cascade="all, delete-orphan"
)