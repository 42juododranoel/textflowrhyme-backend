from __future__ import annotations

import typing

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from textflowrhyme.base.database.model import BaseModel

if typing.TYPE_CHECKING:
    from textflowrhyme.apps.books.models.book import Book
else:
    Book = "Book"


class Page(BaseModel):
    """A page stores textual data."""

    __tablename__ = "books__page"

    # Fields

    content = Column(String(255))

    # Relations

    book_id: Mapped[int] = mapped_column(ForeignKey("books__book.id"))
    book: Mapped[Book] = relationship(back_populates="pages")
