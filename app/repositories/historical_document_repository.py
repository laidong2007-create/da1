from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.historical_document import HistoricalDocument

class HistoricalDocumentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, doc: HistoricalDocument) -> HistoricalDocument:
        self.session.add(doc)
        await self.session.commit()
        await self.session.refresh(doc)
        return doc

    async def get_by_id(self, doc_id: int) -> Optional[HistoricalDocument]:
        result = await self.session.execute(
            select(HistoricalDocument).where(HistoricalDocument.id == doc_id)
        )
        return result.scalars().first()

    async def get_all(self, skip: int = 0, limit: int = 50) -> Sequence[HistoricalDocument]:
        result = await self.session.execute(
            select(HistoricalDocument).offset(skip).limit(limit)
        )
        return result.scalars().all()