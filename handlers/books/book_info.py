from aiogram import Router
from aiogram.types import CallbackQuery

from DatabaseAPI.commands import BooksAPI
from utils.callback_factories.books import SelectBookCallbackFactory
from keyboards.inline.books import BooksInlineKeyboards


router = Router()


@router.callback_query(SelectBookCallbackFactory.filter())
async def book_select(
    call: CallbackQuery, callback_data: SelectBookCallbackFactory
) -> None:
    book = await BooksAPI.select_book(Id=callback_data.BookId)

    await call.message.edit_text(
        f"Информация о книге:\n\nНазвание: {book.Name}\n\nЖанр: {book.genre.Name}\nАвтор: {book.Author}\nОписание: {book.Description}",
        reply_markup=BooksInlineKeyboards.book_remove_back_keyboard(
            book_id=book.Id, back=callback_data.back
        ),
    )
