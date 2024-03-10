from unittest.mock import ANY

from httpx import AsyncClient
from starlette import status

from textflowrhyme.apps.books.models import Page


async def test_list_pages(as_anon: AsyncClient, page: Page):
    response = await as_anon.get("/api/v1.0.0/pages")

    response_json = response.json()
    assert response_json == {
        "collection": [
            {
                "id": page.id,
                "content": "{}",
                "created_at": ANY,
                "updated_at": ANY,
            },
        ],
        "count": 1,
    }
    assert response.status_code == status.HTTP_200_OK


async def test_retrieve_pages(as_anon: AsyncClient, page: Page):
    response = await as_anon.get(f"/api/v1.0.0/pages/{page.id}")

    response_json = response.json()
    assert response_json == {
        "instance": {
            "id": page.id,
            "content": "{}",
            "created_at": ANY,
            "updated_at": ANY,
        },
    }
    assert response.status_code == status.HTTP_200_OK
