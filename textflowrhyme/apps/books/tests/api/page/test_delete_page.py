import pytest
from httpx import AsyncClient
from sqlalchemy.exc import NoResultFound
from starlette import status

from textflowrhyme.apps.books.models import Page
from textflowrhyme.shortcuts.database import database


async def test_delete_page(as_anon: AsyncClient, page: Page):
    response = await as_anon.delete(
        f"/api/v1.0.0/pages/{page.id}",
    )

    assert response.content == b""
    assert response.status_code == status.HTTP_204_NO_CONTENT
    with pytest.raises(NoResultFound):
        database.get(Page, page.id)
