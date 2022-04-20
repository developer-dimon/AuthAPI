from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import database, metadata, engine
from user.routers import user_router

app = FastAPI()
metadata.create_all(engine)
app.state.database = database

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
