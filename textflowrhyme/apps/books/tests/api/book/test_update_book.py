from httpx import AsyncClient
from starlette import status

from textflowrhyme.apps.books.models import Book
from textflowrhyme.shortcuts.database import database


async def test_update_book(as_anon: AsyncClient, book: Book):
    response = await as_anon.patch(
        f"/api/v1.0.0/books/{book.id}",
        json={
            "title": "new title",
        },
    )

    updated_book = database.get(Book, book.id)
    assert response.json() == {
        "instance": {
            "id": updated_book.id,
            "title": "new title",
            "pages": [],
        },
    }
    assert updated_book.as_dict() == {
        "id": book.id,
        "title": "new title",
    }
    assert response.status_code == status.HTTP_200_OK
