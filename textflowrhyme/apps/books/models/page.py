from __future__ import annotations

import typing as t

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from textflowrhyme.base.database.model import Model

if t.TYPE_CHECKING:
    from textflowrhyme.apps.books.models.book import Book
else:
    Book = "Book"


class Page(Model):
    """A page stores textual data."""

    __tablename__ = "books__page"

    # Fields

    content = Column(String(65535))

    # Relations

    book_id: Mapped[int] = mapped_column(ForeignKey("books__book.id"))
    book: Mapped[Book] = relationship(back_populates="pages")
