from fastapi import APIRouter, Depends
from app.services.rag_service import rag_service

router = APIRouter(prefix="/knowledge-search", tags=["Knowledge Search"])

@router.get("/")
async def search_knowledge(query: str, top_k: int = 3):
    """Tìm kiếm tư liệu lịch sử trực tiếp thông qua RAG Service"""
    return rag_service.query(user_query=query, top_k=top_k)