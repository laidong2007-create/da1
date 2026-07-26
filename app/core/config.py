import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Khai báo tất cả các biến có trong file .env của bạn
    PROJECT_NAME: str = "Echoes of War"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    DATABASE_URL: str = "sqlite+aiosqlite:///./echoes_of_war.db"

    # JWT Configs
    SECRET_KEY: str = "your-secret-key-123456"
    JWT_SECRET_KEY: str = "your_super_secret_key_change_me"
    ALGORITHM: str = "HS256"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    # ChromaDB & LLM
    CHROMA_DB_PATH: str = "./chroma_db"
    OPENAI_API_KEY: str = ""

    # Cấu hình Pydantic V2: Cho phép bỏ qua các biến thừa trong .env mà không gây Crash
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"  # Quan trọng
    )


settings = Settings()