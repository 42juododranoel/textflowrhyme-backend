from fastapi import APIRouter, FastAPI

from textflowrhyme.apps.books.api.routers.book import router as book_router
from textflowrhyme.apps.books.api.routers.page import router as page_router
from textflowrhyme.apps.users.api.routers.authentication import router as authentication_router
from textflowrhyme.apps.users.api.routers.user import router as user_router


def get_app() -> FastAPI:
    """Get FastAPI application."""

    api_router = APIRouter()
    api_router.include_router(book_router, prefix="/books")
    api_router.include_router(page_router, prefix="/pages")
    api_router.include_router(authentication_router, prefix="/authentication")
    api_router.include_router(user_router, prefix="/users")

    app = FastAPI()
    app.include_router(router=api_router, prefix="/api/v1.0.0")

    return app


app = get_app()
