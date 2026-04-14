from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def services_stub():
    return {"module": "services"}
