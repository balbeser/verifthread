from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from data.context import MenuKeyboard
from keyboards.reply.menu import ReplyMenuKeyboards
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(CommandStart())
@router.message(F.text == MenuKeyboard.back)
async def start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Привет!", reply_markup=ReplyMenuKeyboards.get_main_menu_markup()
    )
