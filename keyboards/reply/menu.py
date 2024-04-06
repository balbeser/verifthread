from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from data.context import MenuKeyboard


class ReplyMenuKeyboards:
    @staticmethod
    def get_main_menu_markup() -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()
        for text in [MenuKeyboard.__dict__[_] for _ in MenuKeyboard.__annotations__]:
            builder.button(text=text)
        builder.adjust(*MenuKeyboard.adjust)
        return builder.as_markup(resize_keyboard=True)
