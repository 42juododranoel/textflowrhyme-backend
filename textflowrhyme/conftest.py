import pytest
from _pytest.fixtures import SubRequest
from fastapi import FastAPI
from httpx import AsyncClient

from textflowrhyme.app import get_app
from textflowrhyme.shortcuts.database import database


@pytest.fixture(scope="session", autouse=True)
def anyio_backend() -> str:
    """Allow running async tests before each pytest run."""
    return "asyncio"


@pytest.fixture
def app() -> FastAPI:
    """FastAPI app."""
    return get_app()


@pytest.fixture
def as_anon(app: FastAPI) -> AsyncClient:
    """Test client."""
    return AsyncClient(app=app, base_url="http://test")


@pytest.fixture(autouse=True)
def _recreate_tables(request: SubRequest) -> None:
    """Recreate all tables before each test run."""

    database.recreate_tables()
