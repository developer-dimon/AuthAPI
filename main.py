from fastapi import FastAPI
from config import database
from user.api import user_router

app = FastAPI()
app.state.database = database


app.include_router(user_router)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.disconnect()
