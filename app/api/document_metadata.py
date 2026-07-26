from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.document_metadata import DocumentMetadata
from app.schemas.document_metadata import (
    DocumentMetadataCreate,
    DocumentMetadataResponse,
)
from app.repositories.document_metadata_repository import DocumentMetadataRepository

router = APIRouter(prefix="/document-metadata", tags=["Document Metadata"])


@router.post(
    "/document/{document_id}",
    response_model=List[DocumentMetadataResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_document_metadata(
    document_id: int,
    metadata_list: List[DocumentMetadataCreate],
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Thêm danh sách thẻ metadata cho 1 tài liệu lịch sử"""
    repo = DocumentMetadataRepository(db)
    entities = [
        DocumentMetadata(
            document_id=document_id, key=item.key, value=item.value
        )
        for item in metadata_list
    ]
    await repo.add_many(entities)
    return entities


@router.get(
    "/document/{document_id}", response_model=List[DocumentMetadataResponse]
)
async def get_metadata_by_document(
    document_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Lấy danh sách metadata của một tài liệu"""
    stmt = select(DocumentMetadata).where(
        DocumentMetadata.document_id == document_id
    )
    result = await db.execute(stmt)
    return result.scalars().all()


@router.delete("/{metadata_id}", status_code=status.HTTP_200_OK)
async def delete_metadata(
    metadata_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Xóa một thẻ metadata"""
    entity = await db.get(DocumentMetadata, metadata_id)
    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy thẻ metadata",
        )
    await db.delete(entity)
    await db.commit()
    return {"message": "Đã xóa thẻ metadata thành công"}