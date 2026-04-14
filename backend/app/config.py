from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # Database
    DATABASE_URL: str = ""

    # Auth — JWT_SECRET_KEY is required; empty string allows token forgery
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # 7 days

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:8081"]

    # Google OAuth
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""

    # Gemini (BB06)
    GEMINI_API_KEY: str = ""

    # Firebase (BB07)
    FIREBASE_CREDENTIALS: str = ""

    # Internal scheduler
    INTERNAL_API_KEY: str = ""


@lru_cache()
def get_settings() -> Settings:
    """Return cached application settings loaded from environment / .env file."""
    return Settings()
