from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.document_metadata import DocumentMetadata

class DocumentMetadataRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_many(self, metadata_list: List[DocumentMetadata]) -> List[DocumentMetadata]:
        self.session.add_all(metadata_list)
        await self.session.commit()
        for item in metadata_list:
            await self.session.refresh(item)
        return metadata_list