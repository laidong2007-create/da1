from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.document_source import DocumentSource
from app.schemas.document_source import DocumentSourceCreate, DocumentSourceResponse
from app.repositories.document_source_repository import DocumentSourceRepository

router = APIRouter(prefix="/document-sources", tags=["Document Sources"])


@router.post(
    "/document/{document_id}",
    response_model=DocumentSourceResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_document_source(
    document_id: int,
    source_in: DocumentSourceCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Tạo mới nguồn trích dẫn cho tài liệu"""
    repo = DocumentSourceRepository(db)
    source_entity = DocumentSource(
        document_id=document_id,
        source_name=source_in.source_name,
        source_url=source_in.source_url,
    )
    return await repo.create(source_entity)


@router.get(
    "/document/{document_id}", response_model=List[DocumentSourceResponse]
)
async def get_sources_by_document(
    document_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Lấy danh sách nguồn trích dẫn của một tài liệu"""
    stmt = select(DocumentSource).where(
        DocumentSource.document_id == document_id
    )
    result = await db.execute(stmt)
    return result.scalars().all()


@router.delete("/{source_id}", status_code=status.HTTP_200_OK)
async def delete_document_source(
    source_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Xóa nguồn trích dẫn"""
    entity = await db.get(DocumentSource, source_id)
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy nguồn trích dẫn",
        )
    await db.delete(entity)
    await db.commit()
    return {"message": "Đã xóa nguồn trích dẫn thành công"}