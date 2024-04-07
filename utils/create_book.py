from aiogram import Router
from aiogram.types import Message

from DatabaseAPI.commands import BooksAPI
from data.context import AddBookText
from keyboards.reply.menu import ReplyMenuKeyboards

router = Router()


async def create_book(message: Message, **kwargs):
    await BooksAPI.add_book(**kwargs)

    await message.answer(
        AddBookText.book_success_created,
        reply_markup=ReplyMenuKeyboards.get_main_menu_markup(),
    )
