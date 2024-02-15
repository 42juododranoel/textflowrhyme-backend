from textflowrhyme.apps.books.api.serializers.page import PageSerializer
from textflowrhyme.base.api.serializers import Serializer


class BookUpsertSerializer(Serializer):
    title: str | None


class BookSerializer(BookUpsertSerializer):
    id: int
    pages: list[PageSerializer]
