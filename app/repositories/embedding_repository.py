from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.embedding_index import EmbeddingIndex

class EmbeddingRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_or_create_index_info(self) -> EmbeddingIndex:
        result = await self.session.execute(
            select(EmbeddingIndex).where(EmbeddingIndex.collection_name == "knowledge_base")
        )
        index_info = result.scalars().first()
        
        if not index_info:
            index_info = EmbeddingIndex(collection_name="knowledge_base", total_vectors=0)
            self.session.add(index_info)
            await self.session.commit()
            await self.session.refresh(index_info)
            
        return index_info