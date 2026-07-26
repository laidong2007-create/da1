from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.schemas.historical_figure import HistoricalFigureCreate, HistoricalFigureResponse
from app.services.historical_figure_service import HistoricalFigureService

router = APIRouter(prefix="/historical-figures", tags=["Figures"])

@router.post("/", response_model=HistoricalFigureResponse, status_code=201)
async def create_figure(data: HistoricalFigureCreate, db: AsyncSession = Depends(get_db)):
    service = HistoricalFigureService(db)
    return await service.create_figure(data)

@router.get("/", response_model=List[HistoricalFigureResponse])
async def get_figures(db: AsyncSession = Depends(get_db)):
    service = HistoricalFigureService(db)
    return await service.list_figures()