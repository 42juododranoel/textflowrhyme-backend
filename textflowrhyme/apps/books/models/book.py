from __future__ import annotations

import typing as t

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from textflowrhyme.base.database.model import Model

if t.TYPE_CHECKING:
    from textflowrhyme.apps.books.models.page import Page
else:
    Page = "Page"


class Book(Model):
    """A book consists of pages."""

    __tablename__ = "books__book"

    # Fields

    title = Column(String(255))

    # Relations

    pages: Mapped[list[Page]] = relationship(back_populates="book")

    # Meta

    SELECTINS: t.ClassVar = [pages]
