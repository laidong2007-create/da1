from pydantic import BaseModel


class DocumentMetadataBase(BaseModel):
    key: str
    value: str


class DocumentMetadataCreate(DocumentMetadataBase):
    pass


class DocumentMetadataResponse(DocumentMetadataBase):
    id: int
    document_id: int

    class Config:
        from_attributes = True  