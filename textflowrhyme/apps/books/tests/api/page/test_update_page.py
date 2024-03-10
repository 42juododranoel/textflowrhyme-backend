from unittest.mock import ANY

from httpx import AsyncClient
from starlette import status

from textflowrhyme.apps.books.models import Book, Page
from textflowrhyme.shortcuts.database import database


async def test_update_page(as_anon: AsyncClient, page: Page, book: Book):
    response = await as_anon.patch(
        f"/api/v1.0.0/pages/{page.id}",
        json={
            "content": "{}",
        },
    )

    updated_page = database.get(Page, page.id)
    assert response.json() == {
        "instance": {
            "id": updated_page.id,
            "content": "{}",
            "created_at": ANY,
            "updated_at": ANY,
        },
    }
    assert updated_page.as_dict() == {
        "id": page.id,
        "book_id": book.id,
        "content": "{}",
        "created_at": ANY,
        "updated_at": ANY,
    }
    assert response.status_code == status.HTTP_200_OK
