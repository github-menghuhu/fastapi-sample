from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def test_organization():
    return {"message": "Hello World organization api..."}
