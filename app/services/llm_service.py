import json
from openai import OpenAI
from app.core.config import settings

class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate_session_summary(self, conversation_history: str) -> dict:
        """AI Tóm tắt nội dung cuộc trò chuyện lịch sử"""
        prompt = f"""
Dựa vào cuộc trò chuyện lịch sử dưới đây, hãy tóm tắt nội dung chính và đưa ra các bài học lịch sử quan trọng.
Trả về định dạng JSON có cấu trúc như sau:
{{
    "summary": "Tóm tắt ngắn gọn cuộc trò chuyện...",
    "key_takeaways": ["Bài học 1", "Bài học 2", "Bài học 3"]
}}

[LỊCH SỬ TRÒ CHUYỆN]:
{conversation_history}
"""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.3
        )
        return json.loads(response.choices[0].message.content)

    def generate_quiz_from_session(self, conversation_history: str) -> list[dict]:
        """Tự động sinh 3 câu hỏi trắc nghiệm kiểm tra kiến thức từ phiên trò chuyện"""
        prompt = f"""
Dựa vào cuộc trò chuyện lịch sử dưới đây, hãy tạo 3 câu hỏi trắc nghiệm (mỗi câu 4 lựa chọn) để kiểm tra người dùng.
Trả về định dạng JSON dạng danh sách:
{{
    "questions": [
        {{
            "question": "Câu hỏi...",
            "options": ["A...", "B...", "C...", "D..."],
            "correct_option_index": 0,
            "explanation": "Giải thích chi tiết..."
        }}
    ]
}}

[LỊCH SỬ TRÒ CHUYỆN]:
{conversation_history}
"""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.5
        )
        data = json.loads(response.choices[0].message.content)
        return data.get("questions", [])

llm_service = LLMService()