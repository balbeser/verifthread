from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from data.context import ListBooksText, MenuKeyboard
from DatabaseAPI.commands import BooksAPI
from keyboards.inline.books import BooksInlineKeyboards

router = Router()


@router.message(F.text == MenuKeyboard.list_books)
async def books_list(message: Message) -> None:
    books = await BooksAPI.select_books()

    await message.answer(
        ListBooksText.list_books,
        reply_markup=BooksInlineKeyboards.books_list_keyboard(books=books),
    )


@router.callback_query(F.data == "list_books")
async def books_list_callback(call: CallbackQuery) -> None:
    books = await BooksAPI.select_books()

    await call.message.edit_text(
        ListBooksText.list_books,
        reply_markup=BooksInlineKeyboards.books_list_keyboard(books=books),
    )
