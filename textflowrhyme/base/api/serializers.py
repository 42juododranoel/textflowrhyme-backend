import typing

from pydantic import BaseModel

InstanceTypeResult = typing.TypeVar("InstanceTypeResult")


class Serializer(BaseModel):
    """Derive serializers from this."""


class Payload(Serializer):
    """Derive request serializers from this."""


class Result(Serializer):
    """Derive response serializers from this."""


class InstanceResult(Result, typing.Generic[InstanceTypeResult]):
    """Root instance response serializer."""

    instance: InstanceTypeResult


class CollectionResult(Result, typing.Generic[InstanceTypeResult]):
    """Root collection response serializer."""

    collection: list[InstanceTypeResult]
    count: int
