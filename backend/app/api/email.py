from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def email_stub():
    return {"module": "email"}
