import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentProcessingService:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

    def extract_text(self, file_path: str, file_type: str) -> str:
        """Đọc file PDF/TXT/DOCX và chuyển thành văn bản thô"""
        if file_type == "txt":
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        # Có thể mở rộng dùng PyPDF2 hoặc python-docx cho pdf/docx
        return ""

    def chunk_text(self, text: str) -> list[str]:
        """Chia nhỏ tài liệu thành các đoạn Chunk"""
        return self.text_splitter.split_text(text)

document_processing_service = DocumentProcessingService()