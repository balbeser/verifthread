from aiogram import Router
from aiogram.types import CallbackQuery

from data.context import BookInfoText
from DatabaseAPI.commands import BooksAPI
from keyboards.inline.books import BooksInlineKeyboards
from utils.callback_factories.books import SelectBookCallbackFactory

router = Router()


@router.callback_query(SelectBookCallbackFactory.filter())
async def book_select(
    call: CallbackQuery, callback_data: SelectBookCallbackFactory
) -> None:
    book = await BooksAPI.select_book(Id=callback_data.BookId)

    await call.message.edit_text(
        BookInfoText.book_info_format.format(
            name=book.Name,
            genre=book.genre.Name,
            author=book.Author,
            description=book.Description,
        ),
        reply_markup=BooksInlineKeyboards.book_remove_back_keyboard(
            book_id=book.Id, back=callback_data.back
        ),
    )
