from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.repositories.embedding_repository import EmbeddingRepository
from app.vectorstore.chromadb_client import chroma_client

router = APIRouter(prefix="/document-embeddings", tags=["Document Embeddings"])


@router.get("/status", status_code=status.HTTP_200_OK)
async def get_embedding_status(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Lấy trạng thái và tổng số lượng Vector Embeddings đang lưu trữ"""
    repo = EmbeddingRepository(db)
    index_info = await repo.get_or_create_index_info()
    chroma_count = chroma_client.collection.count()

    return {
        "collection_name": index_info.collection_name,
        "total_vectors_in_db": index_info.total_vectors,
        "total_vectors_in_chroma": chroma_count,
        "last_synced_at": index_info.last_synced_at,
    }


@router.delete("/clear", status_code=status.HTTP_200_OK)
async def clear_all_embeddings(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """[Admin/System] Xóa toàn bộ Vector Embeddings khỏi ChromaDB"""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Bạn không có quyền thực hiện thao tác này",
        )

    # Reset collection trong ChromaDB
    all_ids = chroma_client.collection.get()["ids"]
    if all_ids:
        chroma_client.collection.delete(ids=all_ids)

    return {"message": "Đã xóa toàn bộ dữ liệu Vector Embeddings thành công"}