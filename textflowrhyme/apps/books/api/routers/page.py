from fastapi import APIRouter
from starlette import status

from textflowrhyme.apps.books.api.serializers import (
    PageCreatePayload,
    PageResult,
    PageUpdatePayload,
)
from textflowrhyme.apps.books.models import Page
from textflowrhyme.base.api.serializers import CollectionResult, InstanceResult
from textflowrhyme.shortcuts.view import view

router = APIRouter()


@router.get("")
async def list_pages() -> CollectionResult[PageResult]:
    """List pages."""

    return view.list_collection(Page, PageResult)


@router.get("/{page_id}")
async def retrieve_page(
    page_id: Page.Id,
) -> InstanceResult[PageResult]:
    """Retrieve a page."""

    return view.retrieve_instance(Page, page_id, PageResult)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_page(
    payload: PageCreatePayload,
) -> InstanceResult[PageResult]:
    """Create a page."""

    return view.create_instance(Page, payload, PageResult)


@router.patch("/{page_id}")
async def update_page(
    page_id: Page.Id,
    payload: PageUpdatePayload,
) -> InstanceResult[PageResult]:
    """Update a page."""

    return view.update_instance(Page, page_id, payload, PageResult)


@router.delete("/{page_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_page(page_id: Page.Id) -> None:
    """Delete a page."""

    return view.delete_instance(Page, page_id)
