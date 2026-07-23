from fastapi import FastAPI
from app.core.config import settings
from app.api.historical_figures import router as historical_figure_router


app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API for Echoes of War",
    version=settings.APP_VERSION,
)
app.include_router(historical_figure_router)


@app.get("/", tags=["System"])
async def root():
    """
    API kiểm tra trạng thái hoạt động của hệ thống.
    """
    return {
        "status": "success",
        "message": f"{settings.APP_NAME} is running",
        "version": settings.APP_VERSION,
    }


@app.get("/health", tags=["System"])
async def health_check():
    """
    API kiểm tra sức khỏe của server.
    """
    return {
        "status": "healthy"
    }


