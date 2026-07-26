from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.consultation_repository import ConsultationRepository
from app.repositories.historical_figure_repository import HistoricalFigureRepository
from app.services.rag_service import rag_service

class ConsultationService:
    def __init__(self, db: AsyncSession):
        self.consult_repo = ConsultationRepository(db)
        self.figure_repo = HistoricalFigureRepository(db)

    async def chat_with_figure(self, user_id: int, figure_id: int, session_id: int | None, user_message: str):
        figure = await self.figure_repo.get_by_id(figure_id)
        if not figure:
            raise Exception("Không tìm thấy nhân vật lịch sử")

        if not session_id:
            session = await self.consult_repo.create_session(user_id, figure_id, f"Trò chuyện với {figure.name}")
            session_id = session.id

        # RAG Search
        rag_res = rag_service.query(user_message)
        reply = rag_res["answer"]

        # Save History
        await self.consult_repo.add_message(session_id, "user", user_message)
        await self.consult_repo.add_message(session_id, "assistant", reply)

        return {"session_id": session_id, "reply": reply, "sources": rag_res["sources"]}