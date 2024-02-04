from fastapi import APIRouter
from sqlalchemy import select
from starlette import status

from textflowrhyme.apps.books.api.serializers import BookSerializer
from textflowrhyme.apps.books.models.book import Book
from textflowrhyme.base.views.render import render_many, render_one
from textflowrhyme.database.session import Session

router = APIRouter()


@router.get("")
async def list_books():
    """List books."""

    statement = select(Book)
    with Session() as session:
        instances = session.scalars(statement).fetchall()

    return render_many(instances, BookSerializer)


@router.get("/{book_id}")
async def retrieve_book(book_id: int):
    """Retrieve a book."""

    statement = select(Book).where(Book.id == book_id)
    with Session() as session:
        instance = session.scalars(statement).one()

    return render_one(instance, BookSerializer)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_book(payload: dict):
    """Create a book."""

    with Session() as session:
        instance = Book(**payload)
        session.add(instance)
        session.commit()

    return render_one(instance, BookSerializer)
