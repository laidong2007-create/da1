from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import đúng chuẩn 8 API Routers theo cấu trúc thư mục app/api/
from app.api import (
    ai_consultation,
    auth,
    document_embeddings,
    document_metadata,
    document_sources,
    historical_documents,
    historical_figures,
    knowledge_search,
)

app = FastAPI(
    title="Echoes of War - Backend API",
    version="1.0.0",
    description="Hệ thống AI Hội thoại Nhân vật Lịch sử & Quản trị Tri thức RAG",
)

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký chính xác 8 Routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(historical_figures.router, prefix="/api/v1")
app.include_router(historical_documents.router, prefix="/api/v1")
app.include_router(document_metadata.router, prefix="/api/v1")
app.include_router(document_sources.router, prefix="/api/v1")
app.include_router(document_embeddings.router, prefix="/api/v1")
app.include_router(knowledge_search.router, prefix="/api/v1")
app.include_router(ai_consultation.router, prefix="/api/v1")


@app.get("/", tags=["Health Check"])
def root():
    return {
        "project": "Echoes of War",
        "status": "Online",
        "documentation": "/docs",
    }



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)