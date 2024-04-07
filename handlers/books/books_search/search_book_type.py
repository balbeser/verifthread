from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from data.context import MenuKeyboard, SearchBooksText
from keyboards.inline.books import BooksInlineKeyboards

router = Router()


@router.message(F.text == MenuKeyboard.search_book)
async def search_type(message: Message) -> None:
    await message.answer(
        SearchBooksText.select_search_type,
        reply_markup=BooksInlineKeyboards.select_book_search_type(),
    )


@router.callback_query(F.data == "search_book")
async def select_search_type(call: CallbackQuery) -> None:
    await call.message.edit_text(
        SearchBooksText.select_search_type,
        reply_markup=BooksInlineKeyboards.select_book_search_type(),
    )
