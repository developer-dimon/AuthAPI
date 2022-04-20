from fastapi import Depends
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from starlette.requests import Request
from user.models import get_user_db
from user.shemas import UserDB, UserCreate, UserUpdate, User

from config import SECRET_KEY


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: UserDB, request: Request = None):
        print(f"User {user.id} has registered.")

    async def on_after_request_verify(self, user: UserDB, token: str, request: Request = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
current_active_user = fastapi_users.current_user(active=True)
