from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_db
from app.repositories.historical_figure_repository import (
    HistoricalFigureRepository,
)
from app.schemas.historical_figure import (
    HistoricalFigureCreate,
    HistoricalFigureResponse,
    HistoricalFigureUpdate,
)
from app.services.historical_figure_service import (
    HistoricalFigureService,
)

router = APIRouter(
    prefix="/historical-figures",
    tags=["Historical Figures"],
)


def get_service(
    db: AsyncSession = Depends(get_db),
) -> HistoricalFigureService:
    """
    Dependency tạo HistoricalFigureService.
    """
    repository = HistoricalFigureRepository(db)
    return HistoricalFigureService(repository)


@router.get(
    "/",
    response_model=list[HistoricalFigureResponse],
)
async def get_all(
    service: HistoricalFigureService = Depends(get_service),
):
    """
    Lấy toàn bộ nhân vật lịch sử.
    """
    return await service.get_all()


@router.get(
    "/{figure_id}",
    response_model=HistoricalFigureResponse,
)
async def get_by_id(
    figure_id: UUID,
    service: HistoricalFigureService = Depends(get_service),
):
    """
    Lấy nhân vật theo ID.
    """
    try:
        return await service.get_by_id(figure_id)

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.post(
    "/",
    response_model=HistoricalFigureResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    data: HistoricalFigureCreate,
    service: HistoricalFigureService = Depends(get_service),
):
    """
    Tạo nhân vật mới.
    """

    try:
        return await service.create(data)

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.put(
    "/{figure_id}",
    response_model=HistoricalFigureResponse,
)
async def update(
    figure_id: UUID,
    data: HistoricalFigureUpdate,
    service: HistoricalFigureService = Depends(get_service),
):
    """
    Cập nhật nhân vật.
    """

    try:
        return await service.update(
            figure_id,
            data,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.delete(
    "/{figure_id}",
    status_code=status.HTTP_200_OK,
)
async def delete(
    figure_id: UUID,
    service: HistoricalFigureService = Depends(get_service),
):
    """
    Xóa nhân vật.
    """

    try:

        await service.delete(
            figure_id
        )

        return {
            "message": "Xóa nhân vật thành công."
        }

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )