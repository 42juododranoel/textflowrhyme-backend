from enum import StrEnum

from pydantic import Field

from textflowrhyme.base.entities import Entity


class NodeMarkType(StrEnum):
    """A mark can be either length or fatigue."""

    LENGTH = "length"
    FATIGUE = "fatigue"


class NodeMarkAttrs(Entity):
    """Mark attributes store value for mark."""

    value: int | str | list[str]


class NodeMark(Entity):
    """A mark stores additional information about a text node."""

    type: NodeMarkType  # noqa: A003
    attrs: NodeMarkAttrs


class NodeText(Entity):
    """A text is a smallest possible node, containing plain text."""

    type: str = "text"  # noqa: A003
    text: str
    marks: list[NodeMark] = Field(default_factory=list)


class NodeParagraph(Entity):
    """A paragraph node contains multiple text node."""

    type: str = "paragraph"  # noqa: A003
    content: list[NodeText] = Field(default_factory=list)


class NodeDocument(Entity):
    """A document node contains multiple paragraph nodes."""

    type: str = "doc"  # noqa: A003
    content: list[NodeParagraph] = Field(default_factory=list)
