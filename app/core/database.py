from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


# ===========================
# Database Engine
# ===========================

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    future=True,
)


# ===========================
# Session Factory
# ===========================

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


# ===========================
# Base Model
# ===========================

class Base(DeclarativeBase):
    """
    Base class cho tất cả Model.
    """
    pass


# ===========================
# Dependency
# ===========================

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency trả về AsyncSession.
    """

    async with AsyncSessionLocal() as session:
        yield session