from pydantic import BaseModel, ConfigDict
from typing import Optional

class HistoricalFigureBase(BaseModel):
    name: str
    title: str
    era: str
    persona_prompt: str
    bio: str
    avatar_url: Optional[str] = None

class HistoricalFigureCreate(HistoricalFigureBase):
    pass

class HistoricalFigureResponse(HistoricalFigureBase):
    id: int

    model_config = ConfigDict(from_attributes=True)