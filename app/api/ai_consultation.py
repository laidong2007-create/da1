from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.ai_consultation import ConsultationChatRequest, ConsultationChatResponse
from app.services.consultation_service import ConsultationService

router = APIRouter(prefix="/consultation", tags=["AI Consultation"])

@router.post("/chat", response_model=ConsultationChatResponse)
async def chat(req: ConsultationChatRequest, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    service = ConsultationService(db)
    return await service.chat_with_figure(user.id, req.figure_id, req.session_id, req.message)