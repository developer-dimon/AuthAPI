import os
import databases
import sqlalchemy

from dotenv import load_dotenv

load_dotenv('.env')
SECRET_KEY = os.environ.get('SECRET_KEY')

DB_PATH = "sqlite:///sqlite.db"

metadata = sqlalchemy.MetaData()
database = databases.Database(DB_PATH)
engine = sqlalchemy.create_engine(DB_PATH)


# from typing import Any, Dict, Optional
#
# from pydantic import BaseSettings, PostgresDsn, validator


# class Settings(BaseSettings):
#     POSTGRES_SERVER: str
#     POSTGRES_USER: str
#     POSTGRES_PASSWORD: str
#     POSTGRES_DB: str
#
#     SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
#
#     @validator("SQLALCHEMY_DATABASE_URI", pre=True)
#     def assemble_db_connection(self, v: Optional[str], values: Dict[str, Any]) -> Any:
#         if isinstance(v, str):
#             return v
#         return PostgresDsn.build(
#             scheme="postgresql",
#             user=values.get("POSTGRES_USER"),
#             password=values.get("POSTGRES_PASSWORD"),
#             host=values.get("POSTGRES_HOST"),
#             path=f"/{values.get('POSTGRES_DB') or  ''}",
#         )
#
#     class Config:
#         case_sensitive = True
#         env_file = ".env"


# settings = Settings()
