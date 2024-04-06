from sqlalchemy import and_, delete, or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

from ..database import get_session
from ..models import Book, Genre


class BooksAPI:
    @staticmethod
    async def add_book(name: str, author: str, description: str, genre_id: int) -> Book:
        async with get_session() as session:
            book_object = Book(
                Name=name, Author=author, Description=description, GenreId=genre_id
            )
            session.add(book_object)
            try:
                await session.commit()
                return book_object
            except IntegrityError:
                await session.rollback()
                return False

    @staticmethod
    async def select_book(**kwargs) -> Book:
        async with get_session() as session:
            sql = (
                select(Book)
                .join(Genre)
                .where(
                    and_(
                        *[getattr(Book, key) == value for key, value in kwargs.items()]
                    )
                )
                .options(joinedload(Book.genre))
            )
            req = await session.execute(sql)
            return req.scalar_one_or_none()

    @staticmethod
    async def select_books(**kwargs) -> Book:
        async with get_session() as session:
            sql = (
                select(Book)
                .join(Genre)
                .where(
                    and_(
                        *[getattr(Book, key) == value for key, value in kwargs.items()]
                    )
                )
                .options(joinedload(Book.genre))
            )
            req = await session.execute(sql)
            return req.scalars().all()

    @staticmethod
    async def select_books_with_like(keyword: str) -> Book:
        async with get_session() as session:
            sql = select(Book).where(
                or_(
                    Book.Author.ilike(f"%{keyword}%"),
                    Book.Name.ilike(f"%{keyword}%"),
                )
            )
            req = await session.execute(sql)
            return req.scalars().all()

    @staticmethod
    async def delete_book_by_id(book_id: int) -> Book:
        async with get_session() as session:
            sql = delete(Book).where(Book.Id == book_id)
            await session.execute(sql)
            await session.commit()
