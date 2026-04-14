from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, email, internal, services, settings, subscriptions
from app.config import get_settings

tags_metadata = [
    {"name": "Auth", "description": "Google OAuth 로그인/회원가입"},
    {"name": "Email", "description": "Gmail 결제 메일 파싱"},
    {"name": "Subscriptions", "description": "구독 관리 CRUD"},
    {"name": "Services", "description": "서비스 DB 검색"},
    {"name": "Settings", "description": "알림 설정"},
    {"name": "Internal", "description": "스케줄러 내부 API (Railway Cron)"},
]


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    _settings = get_settings()

    application = FastAPI(
        title="빨대뽑기 API",
        description="잔소리형 구독 해지 유도 앱",
        version="1.0.0",
        openapi_tags=tags_metadata,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=_settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(auth.router, prefix="/auth", tags=["Auth"])
    application.include_router(email.router, prefix="/email", tags=["Email"])
    application.include_router(subscriptions.router, prefix="/subscriptions", tags=["Subscriptions"])
    application.include_router(services.router, prefix="/services", tags=["Services"])
    application.include_router(settings.router, prefix="/settings", tags=["Settings"])
    application.include_router(internal.router, prefix="/internal", tags=["Internal"])

    @application.get("/health")
    async def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return application


app = create_app()
