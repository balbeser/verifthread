from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from DatabaseAPI.models import Genre
from data.context import MenuKeyboard
from utils.callback_factories.genres import (
    SelectGenreCallbackFactory,
    SelectGenreSearchFilterCallbackFactory,
)
from utils.keyboard_adjust import get_paginate_rows


class GenresInlineKeyboards:
    @staticmethod
    def add_book_select_genre_keyboard(genres: list[Genre]) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        for genre in genres:
            builder.button(
                text=genre.Name,
                callback_data=SelectGenreCallbackFactory(GenreId=genre.Id),
            )
        builder.button(text=MenuKeyboard.add_custom, callback_data="add-custom-genre")

        builder.adjust(*get_paginate_rows(data=genres))
        return builder.as_markup()

    @staticmethod
    def genre_select_filter(genres: list[Genre]) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        for genre in genres:
            builder.button(
                text=genre.Name,
                callback_data=SelectGenreSearchFilterCallbackFactory(GenreId=genre.Id),
            )
        builder.button(text=MenuKeyboard.back, callback_data="search_book")

        builder.adjust(*get_paginate_rows(data=genres))
        return builder.as_markup()
