from datetime import datetime

from textflowrhyme.apps.books.api.serializers.page import PageResult
from textflowrhyme.base.api.serializers import Payload, Result


class BookUpsertPayload(Payload):
    title: str | None


class BookResult(Result):
    id: int

    title: str
    pages: list[PageResult]

    created_at: datetime
    updated_at: datetime
