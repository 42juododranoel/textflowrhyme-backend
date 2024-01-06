from enum import StrEnum

from pydantic import Field

from textflowrhyme.apps.documents.entities.node import NodeDocument
from textflowrhyme.base.entities import Entity


class TreeSpanSubcategory(StrEnum):
    """A span can represent a word, a whitespace, or a punctuation."""

    WORD = "word"
    WHITESPACE = "whitespace"
    PUNCTUATION = "punctuation"


class TreeContext(Entity):
    """A context represents some important info on user-provided text."""

    paragraph_count: int = 0
    sentence_count: int = 0
    word_count: int = 0
    sentence_lengths: list[int] = Field(default_factory=list)


class TreeSpan(Entity):
    """A span is a word or a punctuation mark."""

    content: str
    subcategory: TreeSpanSubcategory
    category: str = "span"

    fatigue: int | None = None


class TreeSpans(Entity):
    """Use span collection when working with multiple spans."""

    collection: list[TreeSpan] = Field(default_factory=list)
    count: int = 0


class TreeSentence(Entity):
    """A sentence is a collection of spans."""

    content: str
    spans: TreeSpans
    category: str = "sentence"
    length: int | None = None


class TreeSentences(Entity):
    """Use sentence collection when working with multiple sentences."""

    collection: list[TreeSentence | TreeSpan] = Field(default_factory=list)
    count: int = 0


class TreeParagraph(Entity):
    """A paragraph is a collection of sentences."""

    content: str
    sentences: TreeSentences
    category: str = "paragraph"


class TreeParagraphs(Entity):
    """Use paragraph collection when working with multiple paragraphs."""

    collection: list[TreeParagraph] = Field(default_factory=list)
    count: int = 0


class Tree(Entity):
    """A tree is a collection of paragraphs created from document node."""

    document: NodeDocument
    context: TreeContext
    paragraphs: TreeParagraphs
    category: str = "text"
