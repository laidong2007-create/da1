import uuid
from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.consultation_session import ConsultationSession


class User(Base):
    """
    Model người dùng.
    """

    __tablename__ = "users"

    # ==========================
    # Primary Key
    # ==========================

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # ==========================
    # Basic Information
    # ==========================

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # ==========================
    # Permission
    # ==========================

    role: Mapped[str] = mapped_column(
        String(20),
        default="user",
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    # ==========================
    # Relationship
    # ==========================

    consultation_sessions: Mapped[list["ConsultationSession"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return (
            f"User(id={self.id}, "
            f"username='{self.username}', "
            f"email='{self.email}')"
        )