from sqlalchemy import and_, select
from sqlalchemy.exc import IntegrityError

from ..database import get_session
from ..models import Genre


class GenresAPI:

    @staticmethod
    async def add_genre(name: str) -> Genre:
        async with get_session() as session:
            genre = Genre(Name=name)
            session.add(genre)
            try:
                await session.commit()
                return genre
            except IntegrityError as ex:
                await session.rollback()
                return False

    @staticmethod
    async def select_genre(**kwargs) -> Genre:
        async with get_session() as session:
            sql = select(Genre).where(
                and_(*[getattr(Genre, key) == value for key, value in kwargs.items()])
            )
            req = await session.execute(sql)
            return req.scalar_one_or_none()

    @staticmethod
    async def select_genres(**kwargs) -> Genre:
        async with get_session() as session:
            sql = select(Genre).where(
                and_(*[getattr(Genre, key) == value for key, value in kwargs.items()])
            )
            req = await session.execute(sql)
            return req.scalars().all()
