from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def auth_stub() -> dict[str, str]:
    return {"module": "auth"}
