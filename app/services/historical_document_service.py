from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.historical_document_repository import HistoricalDocumentRepository
from app.schemas.historical_document import HistoricalDocumentCreate
from app.models.historical_document import HistoricalDocument

class HistoricalDocumentService:
    def __init__(self, db: AsyncSession):
        self.repo = HistoricalDocumentRepository(db)

    async def create_document(self, data: HistoricalDocumentCreate) -> HistoricalDocument:
        doc = HistoricalDocument(**data.model_dump())
        return await self.repo.create(doc)

    async def list_documents(self):
        return await self.repo.get_all()