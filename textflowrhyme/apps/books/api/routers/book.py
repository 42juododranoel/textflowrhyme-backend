from fastapi import APIRouter
from starlette import status

from textflowrhyme.apps.books.api.serializers import BookResult, BookUpsertPayload
from textflowrhyme.apps.books.models.book import Book
from textflowrhyme.base.api.serializers import CollectionResult, InstanceResult
from textflowrhyme.shortcuts.view import view

router = APIRouter()


@router.get("")
async def list_books() -> CollectionResult[BookResult]:
    """List books."""

    return view.list_collection(Book, BookResult)


@router.get("/{book_id}")
async def retrieve_book(
    book_id: Book.Id,
) -> InstanceResult[BookResult]:
    """Retrieve a book."""

    return view.retrieve_instance(Book, book_id, BookResult)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_book(
    payload: BookUpsertPayload,
) -> InstanceResult[BookResult]:
    """Create a book."""

    return view.create_instance(Book, payload, BookResult)


@router.patch("/{book_id}")
async def update_book(
    book_id: Book.Id,
    payload: BookUpsertPayload,
) -> InstanceResult[BookResult]:
    """Update a book."""

    return view.update_instance(Book, book_id, payload, BookResult)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: Book.Id) -> None:
    """Delete a book."""

    return view.delete_instance(Book, book_id)
