from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def auth_stub():
    return {"module": "auth"}
