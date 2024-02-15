from fastapi import APIRouter, FastAPI

from textflowrhyme.apps.books.api.routers.book import router as book_router


def get_app() -> FastAPI:
    """Get FastAPI application."""

    api_router = APIRouter()
    api_router.include_router(book_router, prefix="/books")

    app = FastAPI()
    app.include_router(router=api_router, prefix="/api/v1.0.0")

    return app


app = get_app()
