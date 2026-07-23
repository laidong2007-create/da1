from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.historical_figure import HistoricalFigure
from app.schemas.historical_figure import (
    HistoricalFigureCreate,
    HistoricalFigureUpdate,
)


class HistoricalFigureRepository:
    """
    Repository thao tác với bảng HistoricalFigure.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    # ==========================
    # CREATE
    # ==========================

    async def create(
        self,
        figure: HistoricalFigureCreate
    ) -> HistoricalFigure:

        db_figure = HistoricalFigure(
            **figure.model_dump()
        )

        self.db.add(db_figure)

        await self.db.commit()

        await self.db.refresh(db_figure)

        return db_figure

    # ==========================
    # GET ALL
    # ==========================

    async def get_all(self):

        result = await self.db.execute(

            select(HistoricalFigure)

            .order_by(HistoricalFigure.created_at.desc())

        )

        return result.scalars().all()

    # ==========================
    # GET BY ID
    # ==========================

    async def get_by_id(
        self,
        figure_id: UUID
    ):

        result = await self.db.execute(

            select(HistoricalFigure)

            .where(
                HistoricalFigure.id == figure_id
            )

        )

        return result.scalar_one_or_none()

    # ==========================
    # UPDATE
    # ==========================

    async def update(
        self,
        db_figure: HistoricalFigure,
        data: HistoricalFigureUpdate
    ):

        update_data = data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():

            setattr(
                db_figure,
                key,
                value
            )

        await self.db.commit()

        await self.db.refresh(db_figure)

        return db_figure

    # ==========================
    # DELETE
    # ==========================

    async def delete(
        self,
        db_figure: HistoricalFigure
    ):

        await self.db.delete(db_figure)

        await self.db.commit()

    # ==========================
    # SEARCH
    # ==========================

    async def search_by_name(
        self,
        keyword: str
    ):

        result = await self.db.execute(

            select(HistoricalFigure)

            .where(
                HistoricalFigure.name.ilike(
                    f"%{keyword}%"
                )
            )

        )

        return result.scalars().all()