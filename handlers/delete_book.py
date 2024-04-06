from aiogram import Router
from aiogram.types import CallbackQuery

from DatabaseAPI.commands import BooksAPI
from utils.callback_factories.books import DeleteBookCallbackFactory
from keyboards.inline.books import BooksInlineKeyboards

router = Router()


@router.callback_query(DeleteBookCallbackFactory.filter())
async def book_delete(
    call: CallbackQuery, callback_data: DeleteBookCallbackFactory
) -> None:
    book = await BooksAPI.select_book(Id=callback_data.BookId)
    await BooksAPI.delete_book_by_id(book_id=book.Id)
    await call.message.edit_text(
        f"Книга: {book.Name} успешно удалена!",
        reply_markup=BooksInlineKeyboards.back_books_list_keyboard(),
    )
