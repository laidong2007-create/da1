from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.historical_figure import HistoricalFigure

class HistoricalFigureRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, figure: HistoricalFigure) -> HistoricalFigure:
        self.session.add(figure)
        await self.session.commit()
        await self.session.refresh(figure)
        return figure

    async def get_by_id(self, figure_id: int) -> Optional[HistoricalFigure]:
        result = await self.session.execute(select(HistoricalFigure).where(HistoricalFigure.id == figure_id))
        return result.scalars().first()

    async def get_all(self, skip: int = 0, limit: int = 50) -> Sequence[HistoricalFigure]:
        result = await self.session.execute(select(HistoricalFigure).offset(skip).limit(limit))
        return result.scalars().all()