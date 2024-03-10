from unittest.mock import ANY

from httpx import AsyncClient
from starlette import status

from textflowrhyme.apps.books.models import Book
from textflowrhyme.shortcuts.database import database


async def test_create_book(as_anon: AsyncClient):
    response = await as_anon.post(
        "/api/v1.0.0/books",
        json={
            "title": "On Writing Well",
        },
    )

    response_json = response.json()
    created_book = database.get(Book)
    assert response_json == {
        "instance": {
            "id": created_book.id,
            "title": "On Writing Well",
            "pages": [],
            "created_at": ANY,
            "updated_at": ANY,
        },
    }
    assert created_book.as_dict() == {
        "id": created_book.id,
        "title": "On Writing Well",
        "created_at": ANY,
        "updated_at": ANY,
    }
    assert response.status_code == status.HTTP_201_CREATED
