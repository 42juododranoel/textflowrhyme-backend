import os

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Project settings."""

    database_name: str = os.getenv("DATABASE_NAME", "textflowrhyme")
    database_username: str = os.getenv("DATABASE_USERNAME", "postgres")
    database_password: str = os.getenv("DATABASE_PASSWORD", "password1234")
    database_host: str = os.getenv("DATABASE_HOST", "localhost")
    database_port: str = os.getenv("DATABASE_PORT", "5432")
    database_dsn: PostgresDsn = f"postgresql://{database_username}:{database_password}@{database_host}:{database_port}/{database_name}"


settings = Settings()
