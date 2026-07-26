from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.models.consultation_session import ConsultationSession
from app.models.consultation_message import ConsultationMessage

class ConsultationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_session(self, user_id: int, figure_id: int, title: str) -> ConsultationSession:
        session = ConsultationSession(user_id=user_id, figure_id=figure_id, title=title)
        self.session.add(session)
        await self.session.commit()
        await self.session.refresh(session)
        return session

    async def add_message(self, session_id: int, sender: str, content: str) -> ConsultationMessage:
        msg = ConsultationMessage(session_id=session_id, sender=sender, content=content)
        self.session.add(msg)
        await self.session.commit()
        await self.session.refresh(msg)
        return msg

    async def get_session_by_id(self, session_id: int) -> Optional[ConsultationSession]:
        stmt = select(ConsultationSession).options(selectinload(ConsultationSession.messages)).where(ConsultationSession.id == session_id)
        result = await self.session.execute(stmt)
        return result.scalars().first()