from aiogram import Router
from aiogram.types import Message

from DatabaseAPI.commands import BooksAPI
from keyboards.reply.menu import ReplyMenuKeyboards

router = Router()


async def create_book(message: Message, **kwargs):
    await BooksAPI.add_book(**kwargs)

    await message.answer(
        "Книга успешно создана!", reply_markup=ReplyMenuKeyboards.get_main_menu_markup()
    )
