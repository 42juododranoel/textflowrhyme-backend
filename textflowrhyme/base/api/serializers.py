from pydantic import BaseModel


class Serializer(BaseModel):
    """Serializer base class."""


class RequestSerializer(Serializer):
    """Derive request serializers from this."""


class ResponseSerializer(Serializer):
    """Derive response serializers from this."""
