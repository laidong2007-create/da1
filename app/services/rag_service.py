from app.services.llm_service import llm_service
from app.vectorstore.chromadb_client import chroma_client


class RAGService:

    def query(self, user_query: str, top_k: int = 3) -> dict:
        # 1. Truy vấn Vector từ ChromaDB
        results = chroma_client.query_similar(
            query_text=user_query, n_results=top_k
        )

        docs = results.get("documents", [[]])[0]
        metas = results.get("metadatas", [[]])[0]

        context = (
            "\n---\n".join(docs) if docs else "Không tìm thấy tư liệu liên quan."
        )
        sources = list(
            set([m.get("title", "Tài liệu lịch sử") for m in metas])
        )

        # 2. Xây dựng Prompt cho LLM
        prompt = f"""
Bạn là chuyên gia tư vấn lịch sử Việt Nam. Trả lời câu hỏi dựa vào thông tin tư liệu dưới đây:
[TƯ LIỆU]:
{context}

[CÂU HỎI]:
{user_query}
"""
        # 3. Tạo câu trả lời từ LLM
        answer = llm_service.generate_answer(prompt)
        return {"query": user_query, "answer": answer, "sources": sources}


# Khởi tạo instance rag_service chính xác để các file khác import
rag_service = RAGService()