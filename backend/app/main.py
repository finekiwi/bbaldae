from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, email, internal, services, settings, subscriptions

tags_metadata = [
    {"name": "Auth", "description": "Google OAuth 로그인/회원가입"},
    {"name": "Email", "description": "Gmail 결제 메일 파싱"},
    {"name": "Subscriptions", "description": "구독 관리 CRUD"},
    {"name": "Services", "description": "서비스 DB 검색"},
    {"name": "Settings", "description": "알림 설정"},
    {"name": "Internal", "description": "스케줄러 내부 API (Railway Cron)"},
]

app = FastAPI(
    title="빨대뽑기 API",
    description="잔소리형 구독 해지 유도 앱",
    version="1.0.0",
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서 제한 필요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(email.router, prefix="/email", tags=["Email"])
app.include_router(subscriptions.router, prefix="/subscriptions", tags=["Subscriptions"])
app.include_router(services.router, prefix="/services", tags=["Services"])
app.include_router(settings.router, prefix="/settings", tags=["Settings"])
app.include_router(internal.router, prefix="/internal", tags=["Internal"])


@app.get("/health")
async def health_check():
    return {"status": "ok"}
