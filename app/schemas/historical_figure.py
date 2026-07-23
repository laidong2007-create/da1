from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class HistoricalFigureBase(BaseModel):
    """
    Schema cơ sở của Historical Figure.
    """

    name: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Tên nhân vật lịch sử"
    )

    birth_year: int | None = Field(
        default=None,
        description="Năm sinh"
    )

    death_year: int | None = Field(
        default=None,
        description="Năm mất"
    )

    description: str = Field(
        ...,
        min_length=10,
        description="Mô tả"
    )

    image_url: str | None = Field(
        default=None,
        description="Ảnh đại diện"
    )


class HistoricalFigureCreate(HistoricalFigureBase):
    """
    Schema tạo mới.
    """
    pass


class HistoricalFigureUpdate(BaseModel):
    """
    Schema cập nhật.
    """

    name: str | None = None

    birth_year: int | None = None

    death_year: int | None = None

    description: str | None = None

    image_url: str | None = None


class HistoricalFigureResponse(HistoricalFigureBase):
    """
    Schema trả về.
    """

    id: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )