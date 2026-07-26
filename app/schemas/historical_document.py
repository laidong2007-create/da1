from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

class HistoricalDocumentBase(BaseModel):
    title: str
    content: str
    era: Optional[str] = None

class HistoricalDocumentCreate(HistoricalDocumentBase):
    pass

class HistoricalDocumentResponse(HistoricalDocumentBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)