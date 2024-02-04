from sqlalchemy.orm import Mapped, mapped_column

from textflowrhyme.database.model import BaseModel


class Book(BaseModel):
    __tablename__ = "books__book"

    id: Mapped[int] = mapped_column(primary_key=True)
