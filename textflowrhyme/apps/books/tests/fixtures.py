import pytest

from textflowrhyme.apps.books.models.book import Book
from textflowrhyme.database.session import Session


@pytest.fixture
def book() -> Book:
    with Session() as session:
        book = Book()
        session.add(book)
        session.commit()

    return book
