from textflowrhyme.base.api.serializers import Serializer


class PageUpsertSerializer(Serializer):
    content: str | None


class PageSerializer(PageUpsertSerializer):
    id: int
