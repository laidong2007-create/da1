from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.historical_figure_repository import HistoricalFigureRepository
from app.schemas.historical_figure import HistoricalFigureCreate
from app.models.historical_figure import HistoricalFigure

class HistoricalFigureService:
    def __init__(self, db: AsyncSession):
        self.repo = HistoricalFigureRepository(db)

    async def create_figure(self, data: HistoricalFigureCreate) -> HistoricalFigure:
        figure = HistoricalFigure(**data.model_dump())
        return await self.repo.create(figure)

    async def list_figures(self):
        return await self.repo.get_all()