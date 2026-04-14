from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def subscriptions_stub():
    return {"module": "subscriptions"}
