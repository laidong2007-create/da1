from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.schemas.historical_document import HistoricalDocumentCreate, HistoricalDocumentResponse
from app.services.historical_document_service import HistoricalDocumentService

router = APIRouter(prefix="/historical-documents", tags=["Historical Documents"])

@router.post("/", response_model=HistoricalDocumentResponse, status_code=status.HTTP_201_CREATED)
async def create_document(data: HistoricalDocumentCreate, db: AsyncSession = Depends(get_db)):
    service = HistoricalDocumentService(db)
    return await service.create_document(data)

@router.get("/", response_model=List[HistoricalDocumentResponse])
async def get_documents(db: AsyncSession = Depends(get_db)):
    service = HistoricalDocumentService(db)
    return await service.list_documents()