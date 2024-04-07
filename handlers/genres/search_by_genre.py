from aiogram import F, Router
from aiogram.types import CallbackQuery

from data.context import ListBooksText, SearchBooksText
from DatabaseAPI.commands import BooksAPI, GenresAPI
from keyboards.inline.books import BooksInlineKeyboards
from keyboards.inline.genres import GenresInlineKeyboards
from utils.callback_factories.books import SelectBookSearchTypeCallbackFactory
from utils.callback_factories.genres import SelectGenreSearchFilterCallbackFactory

router = Router()


@router.callback_query(
    SelectBookSearchTypeCallbackFactory.filter(F.search_type == "genre")
)
async def search_type_genre(call: CallbackQuery) -> None:
    genres = await GenresAPI.select_genres()

    await call.message.edit_text(
        SearchBooksText.enter_search_genre,
        reply_markup=GenresInlineKeyboards.genre_select_filter(genres=genres),
    )


@router.callback_query(SelectGenreSearchFilterCallbackFactory.filter())
async def books_genre(
    call: CallbackQuery, callback_data: SelectGenreSearchFilterCallbackFactory
) -> None:
    genre_info = await GenresAPI.select_genre(Id=callback_data.GenreId)
    books = await BooksAPI.select_books(GenreId=callback_data.GenreId)

    await call.message.edit_text(
        ListBooksText.list_books_by_genre,
        reply_markup=BooksInlineKeyboards.books_list_keyboard(books=books, back=False),
    )
