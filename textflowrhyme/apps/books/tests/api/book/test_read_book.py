from httpx import AsyncClient
from starlette import status

from textflowrhyme.apps.books.models import Book, Page


async def test_list_books(as_anon: AsyncClient, book: Book, page: Page):
    response = await as_anon.get("/api/v1.0.0/books")

    response_json = response.json()
    assert response_json == {
        "collection": [
            {
                "id": book.id,
                "title": "On Writing Well",
                "pages": [{"content": "{}", "id": 1}],
            },
        ],
        "count": 1,
    }
    assert response.status_code == status.HTTP_200_OK


async def test_retrieve_books(as_anon: AsyncClient, book: Book, page: Page):
    response = await as_anon.get(f"/api/v1.0.0/books/{book.id}")

    response_json = response.json()
    assert response_json == {
        "instance": {
            "id": book.id,
            "title": "On Writing Well",
            "pages": [{"content": "{}", "id": 1}],
        },
    }
    assert response.status_code == status.HTTP_200_OK
