from fastapi import APIRouter

from user.auth import auth_backend, fastapi_users

user_router = APIRouter()

user_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
user_router.include_router(fastapi_users.get_register_router(), prefix="/auth", tags=["auth"])
user_router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])
