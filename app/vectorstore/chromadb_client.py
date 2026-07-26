import chromadb
from app.core.config import settings

class ChromaClient:
    def __init__(self):
        # Khởi tạo Chroma Persistent Client
        self.client = chromadb.PersistentClient(path="./vectorstore/chroma_db")
        self.collection = self.client.get_or_create_collection(
            name="history_knowledge_base",
            metadata={"hnsw:space": "cosine"}
        )

    def add_chunks(self, ids: list[str], documents: list[str], metadatas: list[dict]):
        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )

    def query_similar(self, query_text: str, n_results: int = 4, where_filter: dict = None):
        return self.collection.query(
            query_texts=[query_text],
            n_results=n_results,
            where=where_filter
        )

    def delete_by_document_id(self, doc_id: int):
        self.collection.delete(where={"document_id": doc_id})

chroma_client = ChromaClient()