from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from data.context import MenuKeyboard
from DatabaseAPI.commands import BooksAPI, GenresAPI
from keyboards.inline.books import BooksInlineKeyboards
from keyboards.inline.genres import GenresInlineKeyboards
from utils.callback_factories.books import SelectBookSearchTypeCallbackFactory
from utils.callback_factories.genres import SelectGenreSearchFilterCallbackFactory
from states.book import SearchState

router = Router()


@router.message(F.text == MenuKeyboard.search_book)
async def search_type(message: Message) -> None:
    await message.answer(
        "Выберите тип поиска:",
        reply_markup=BooksInlineKeyboards.select_book_search_type(),
    )


@router.callback_query(F.data == "search_book")
async def select_search_type(call: CallbackQuery) -> None:
    await call.message.edit_text(
        "Выберите тип поиска:",
        reply_markup=BooksInlineKeyboards.select_book_search_type(),
    )


@router.callback_query(
    SelectBookSearchTypeCallbackFactory.filter(F.search_type == "genre")
)
async def search_type_genre(call: CallbackQuery) -> None:
    genres = await GenresAPI.select_genres()

    await call.message.edit_text(
        "Выберите жанр для поиска:",
        reply_markup=GenresInlineKeyboards.genre_select_filter(genres=genres),
    )


@router.callback_query(SelectGenreSearchFilterCallbackFactory.filter())
async def books_genre(
    call: CallbackQuery, callback_data: SelectGenreSearchFilterCallbackFactory
) -> None:
    genre_info = await GenresAPI.select_genre(Id=callback_data.GenreId)
    books = await BooksAPI.select_books(GenreId=callback_data.GenreId)

    await call.message.edit_text(
        f"Книги с жанром: {genre_info.Name}",
        reply_markup=BooksInlineKeyboards.books_list_keyboard(books=books, back=False),
    )


@router.callback_query(
    SelectBookSearchTypeCallbackFactory.filter(F.search_type == "word_or_phrase")
)
async def search_type_word_or_phrase(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.edit_text("Напишите фразу для поиска:")

    await state.set_state(SearchState.keyword)


@router.message(SearchState.keyword)
async def keyword_search(message: Message, state: FSMContext):
    await state.clear()

    books = await BooksAPI.select_books_with_like(keyword=message.text)

    await message.answer(
        text="Список книг:",
        reply_markup=BooksInlineKeyboards.books_list_keyboard(books=books, back=False),
    )
