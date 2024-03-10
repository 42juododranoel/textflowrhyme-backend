from unittest.mock import ANY

from httpx import AsyncClient
from starlette import status

from textflowrhyme.apps.books.models import Book, Page
from textflowrhyme.shortcuts.database import database


async def test_create_page(as_anon: AsyncClient, book: Book):
    response = await as_anon.post(
        "/api/v1.0.0/pages",
        json={
            "book_id": book.id,
            "content": "{}",
        },
    )

    response_json = response.json()
    created_page = database.get(Page)
    assert response_json == {
        "instance": {
            "id": created_page.id,
            "content": "{}",
            "created_at": ANY,
            "updated_at": ANY,
        },
    }
    assert created_page.as_dict() == {
        "id": created_page.id,
        "content": "{}",
        "book_id": book.id,
        "created_at": ANY,
        "updated_at": ANY,
    }
    assert response.status_code == status.HTTP_201_CREATED
