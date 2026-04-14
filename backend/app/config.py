from functools import lru_cache

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # Database
    DATABASE_URL: str = ""

    # Auth — JWT_SECRET_KEY is required; empty string allows token forgery
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # 7 days

    # CORS — comma-separated origins string (pydantic-settings parses list[str] as JSON only)
    # e.g. CORS_ORIGINS=http://localhost:8081,https://app.example.com
    CORS_ORIGINS: str = "http://localhost:8081"

    @computed_field
    @property
    def cors_origins_list(self) -> list[str]:
        """Return CORS_ORIGINS parsed as a list (split on comma)."""
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]

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
