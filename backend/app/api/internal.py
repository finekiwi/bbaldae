from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def internal_stub() -> dict[str, str]:
    return {"module": "internal"}
