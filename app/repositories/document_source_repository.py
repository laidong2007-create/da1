from sqlalchemy.ext.asyncio import AsyncSession
from app.models.document_source import DocumentSource

class DocumentSourceRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, source: DocumentSource) -> DocumentSource:
        self.session.add(source)
        await self.session.commit()
        await self.session.refresh(source)
        return source