from fastapi import APIRouter

user_router = APIRouter()


@user_router.get('/login')
async def login():
    return {"hi": "hi"}
