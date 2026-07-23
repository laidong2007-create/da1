from uuid import UUID

from app.repositories.historical_figure_repository import (
    HistoricalFigureRepository,
)
from app.schemas.historical_figure import (
    HistoricalFigureCreate,
    HistoricalFigureUpdate,
)


class HistoricalFigureService:
    """
    Service xử lý nghiệp vụ của Historical Figure.
    """

    def __init__(self, repository: HistoricalFigureRepository):
        self.repository = repository

    # ==========================================
    # CREATE
    # ==========================================

    async def create(
        self,
        data: HistoricalFigureCreate,
    ):

        # Kiểm tra tên đã tồn tại chưa
        figures = await self.repository.search_by_name(data.name)

        for figure in figures:
            if figure.name.lower() == data.name.lower():
                raise ValueError(
                    "Tên nhân vật lịch sử đã tồn tại."
                )

        # Kiểm tra năm sinh và năm mất
        if (
            data.birth_year is not None
            and data.death_year is not None
            and data.birth_year > data.death_year
        ):
            raise ValueError(
                "Năm sinh không được lớn hơn năm mất."
            )

        return await self.repository.create(data)

    # ==========================================
    # GET ALL
    # ==========================================

    async def get_all(self):

        return await self.repository.get_all()

    # ==========================================
    # GET BY ID
    # ==========================================

    async def get_by_id(
        self,
        figure_id: UUID,
    ):

        figure = await self.repository.get_by_id(figure_id)

        if figure is None:
            raise ValueError(
                "Không tìm thấy nhân vật."
            )

        return figure

    # ==========================================
    # UPDATE
    # ==========================================

    async def update(
        self,
        figure_id: UUID,
        data: HistoricalFigureUpdate,
    ):

        db_figure = await self.repository.get_by_id(
            figure_id
        )

        if db_figure is None:
            raise ValueError(
                "Không tìm thấy nhân vật."
            )

        return await self.repository.update(
            db_figure,
            data,
        )

    # ==========================================
    # DELETE
    # ==========================================

    async def delete(
        self,
        figure_id: UUID,
    ):

        db_figure = await self.repository.get_by_id(
            figure_id
        )

        if db_figure is None:
            raise ValueError(
                "Không tìm thấy nhân vật."
            )

        await self.repository.delete(
            db_figure
        )

    # ==========================================
    # SEARCH
    # ==========================================

    async def search(
        self,
        keyword: str,
    ):

        return await self.repository.search_by_name(
            keyword
        )