import ormar
from fastapi_users_db_ormar import OrmarBaseUserModel, OrmarUserDatabase
from config import database, metadata
from user.shemas import UserDB


class User(OrmarBaseUserModel):
    class Meta:
        tablename = "users"
        metadata = metadata
        database = database

    username: str = ormar.String(max_length=100, unique=True)


async def get_user_db():
    yield OrmarUserDatabase(UserDB, User)

