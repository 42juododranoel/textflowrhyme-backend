from textflowrhyme.base.api.serializers import Payload, Result


class PageUpsertPayload(Payload):
    content: str | None


class PageResult(Result):
    id: int
    content: str
