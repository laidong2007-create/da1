from pydantic import BaseModel
from typing import Optional

class DocumentSourceBase(BaseModel):
    source_name: str
    source_url: Optional[str] = None

class DocumentSourceCreate(DocumentSourceBase):
    pass

class DocumentSourceResponse(DocumentSourceBase):
    id: int
    document_id: int

    class Config:
        from_attributes = True