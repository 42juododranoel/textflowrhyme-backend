import typing

from pydantic import BaseModel

InstanceSerializerType = typing.TypeVar("InstanceSerializerType")


class Serializer(BaseModel):
    """Derive serializers from this."""


class RequestSerializer(Serializer):
    """Derive request serializers from this."""


class UpsertSerializer(RequestSerializer):
    """Derive create and update serializers from this."""


class CreateSerializer(UpsertSerializer):
    """Derive create serializers from this."""


class UpdateSerializer(UpsertSerializer):
    """Derive update serializers from this."""


class ResponseSerializer(Serializer):
    """Derive response serializers from this."""


class InstanceResponseSerializer(ResponseSerializer, typing.Generic[InstanceSerializerType]):
    """Root instance response serializer."""

    instance: InstanceSerializerType


class CollectionResponseSerializer(ResponseSerializer, typing.Generic[InstanceSerializerType]):
    """Root collection response serializer."""

    collection: list[InstanceSerializerType]
    count: int
