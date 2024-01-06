from fastapi import APIRouter, FastAPI

from textflowrhyme.apps.documents.api.routers.document import router as document_router
from textflowrhyme.apps.texts.api.routers.text import router as text_router


def get_app() -> FastAPI:
    """Get FastAPI application."""

    api_router = APIRouter()
    api_router.include_router(document_router, prefix="/documents")
    api_router.include_router(text_router, prefix="/texts")

    app = FastAPI()
    app.include_router(router=api_router, prefix="/api/v1.0.0")

    return app


app = get_app()
