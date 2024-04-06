import enum
import datetime
from typing import Annotated, List, Optional

from sqlalchemy import ForeignKey, text, BigInteger, event
from sqlalchemy.orm import mapped_column, Mapped, relationship

from DatabaseAPI.database import Base

INTPK = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class Book(Base):
    __tablename__ = "books"

    Id: Mapped[INTPK]
    Name: Mapped[str] = mapped_column(unique=True)
    Author: Mapped[str]
    Description: Mapped[str]

    GenreId: Mapped[int] = mapped_column(ForeignKey("genres.Id"))
    genre: Mapped["Genre"] = relationship(back_populates="books")

    genre: Mapped["Genre"] = relationship(
        back_populates="books",
        foreign_keys=[GenreId],
        primaryjoin="Book.GenreId == Genre.Id",
    )

    def __repr__(self) -> str:
        return f"[{self.Id}] - {self.Name} - {self.Author} -- {self.GenreId}"


class Genre(Base):
    __tablename__ = "genres"

    Id: Mapped[INTPK]
    Name: Mapped[str] = mapped_column(unique=True)

    books: Mapped[Optional[List["Book"]]] = relationship(
        back_populates="genre", foreign_keys=[Book.GenreId]
    )

    def __repr__(self) -> str:
        return f"[{self.Id}] - {self.Name}"
