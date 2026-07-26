from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class ConsultationChatRequest(BaseModel):
    figure_id: int
    session_id: Optional[int] = None
    message: str

class ConsultationMessageResponse(BaseModel):
    id: int
    sender: str
    content: str

    model_config = ConfigDict(from_attributes=True)

class ConsultationChatResponse(BaseModel):
    session_id: int
    reply: str
    sources: List[str] = []