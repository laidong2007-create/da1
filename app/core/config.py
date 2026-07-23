from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Quản lý toàn bộ cấu hình của ứng dụng.
    Các giá trị được đọc từ file .env.
    """

    # ===========================
    # Application
    # ===========================
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    # ===========================
    # Database
    # ===========================
    DATABASE_URL: str

    # ===========================
    # JWT
    # ===========================
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # ===========================
    # OpenAI
    # ===========================
    OPENAI_API_KEY: str = ""

    # ===========================
    # ChromaDB
    # ===========================
    CHROMA_DB_PATH: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()