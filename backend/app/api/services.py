from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def services_stub() -> dict[str, str]:
    return {"module": "services"}
