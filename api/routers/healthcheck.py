from fastapi import APIRouter

router = APIRouter()


@router.head("/healthcheck", tags=["admin"])
async def healthcheck():
    return 200


@router.get("/hello/{name}", tags=["admin"])
async def greeting(name: str):
    return {"greetings": name}
