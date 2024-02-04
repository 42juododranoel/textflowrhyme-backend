from httpx import AsyncClient
from sqlalchemy import select
from starlette import status

from textflowrhyme.apps.books.models.book import Book
from textflowrhyme.database.session import Session


async def test_create_book(as_anon: AsyncClient):
    response = await as_anon.post(
        "/api/v1.0.0/books",
        json={},
    )

    response_json = response.json()
    statement = select(Book)
    with Session() as session:
        instance = session.scalars(statement).one()
    assert response_json == {"id": instance.id}
    assert response.status_code == status.HTTP_201_CREATED
