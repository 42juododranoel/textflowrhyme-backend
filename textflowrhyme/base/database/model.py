import typing as t
from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Model(DeclarativeBase):
    """Base model to derive others from."""

    # Fields

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )
    updated_at = Column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
    )

    # Relations

    # Meta

    SELECTINS: t.ClassVar[list[str]] = []

    # Types

    Id: t.TypeAlias = int

    # Methods

    def as_dict(self) -> dict[str, t.Any]:
        result = {}
        for key, value in self.__dict__.items():
            if key == "_sa_instance_state":
                continue
            if isinstance(value, list):
                result[key] = [
                    subvalue.as_dict() if isinstance(subvalue, Model) else subvalue
                    for subvalue in value
                ]
            else:
                result[key] = value

        return result
