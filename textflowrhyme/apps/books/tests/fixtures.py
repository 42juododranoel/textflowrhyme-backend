import pytest

from textflowrhyme.apps.books.models import Book, Page
from textflowrhyme.base.database.session import Session


@pytest.fixture
def book() -> Book:
    with Session() as session:
        book = Book(
            title="On Writing Well",
        )
        session.add(book)
        session.commit()

    return book


@pytest.fixture
def page(book: Book) -> Page:
    with Session() as session:
        page = Page(
            content="{}",
            book=book,
        )
        session.add(page)
        session.commit()

    return page
