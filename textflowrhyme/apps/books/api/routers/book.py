from fastapi import APIRouter
from starlette import status

from textflowrhyme.apps.books.api.serializers import (
    BookSerializer,
    BookUpsertSerializer,
)
from textflowrhyme.apps.books.models.book import Book
from textflowrhyme.base.api.serializers import (
    CollectionResponseSerializer,
    InstanceResponseSerializer,
)
from textflowrhyme.shortcuts.view import view

router = APIRouter()


@router.get("")
async def list_books() -> CollectionResponseSerializer[BookSerializer]:
    """List books."""

    return view.list_collection(Book, BookSerializer)


@router.get("/{book_id}")
async def retrieve_book(
    book_id: Book.Id,
) -> InstanceResponseSerializer[BookSerializer]:
    """Retrieve a book."""

    return view.retrieve_instance(Book, book_id, BookSerializer)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_book(
    payload: BookUpsertSerializer,
) -> InstanceResponseSerializer[BookSerializer]:
    """Create a book."""

    return view.create_instance(Book, payload, BookSerializer)


@router.patch("/{book_id}")
async def update_book(
    book_id: Book.Id,
    payload: BookUpsertSerializer,
) -> InstanceResponseSerializer[BookSerializer]:
    """Update a book."""

    return view.update_instance(Book, book_id, payload, BookSerializer)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: Book.Id) -> None:
    """Delete a book."""

    return view.delete_instance(Book, book_id)
