from textflowrhyme.base.api.serializers import Payload, Result


class PageCreatePayload(Payload):
    content: str
    book_id: int


class PageUpdatePayload(Payload):
    content: str | None = None
    book_id: int | None = None


class PageResult(Result):
    id: int
    content: str
