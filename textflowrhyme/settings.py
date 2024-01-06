from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Project settings."""


settings = Settings()
