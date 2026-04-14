from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def email_stub() -> dict[str, str]:
    return {"module": "email"}
