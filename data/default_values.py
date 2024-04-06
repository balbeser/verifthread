from enum import Enum


class Genres:
    FANTASY = "🔮 Фантастика"
    DRAMA = "😔 Драма"
    ROMANCE = "💠 Роман"

    genres_list = (FANTASY, DRAMA, ROMANCE)


class BookSearchTypes(Enum):
    WORD_OR_PHRASE = "💠 Слово или фраза"
    GENRE = "💠 По жанру"
