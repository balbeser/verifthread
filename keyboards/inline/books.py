from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from DatabaseAPI.models import Book
from data.context import MenuKeyboard
from data.default_values import BookSearchTypes
from utils.callback_factories.books import (
    SelectBookCallbackFactory,
    DeleteBookCallbackFactory,
    SelectBookSearchTypeCallbackFactory,
)
from utils.keyboard_adjust import get_paginate_rows


class BooksInlineKeyboards:
    @staticmethod
    def books_list_keyboard(
        books: list[Book], back: bool = True
    ) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        for book in books:
            builder.button(
                text=MenuKeyboard.book_info_format.format(
                    name=book.Name, author=book.Author
                ),
                callback_data=SelectBookCallbackFactory(BookId=book.Id, back=back),
            )
        builder.adjust(*get_paginate_rows(data=books, height=2))
        return builder.as_markup()

    @staticmethod
    def book_remove_back_keyboard(book_id: int, back: bool) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(
            text=MenuKeyboard.remove,
            callback_data=DeleteBookCallbackFactory(BookId=book_id),
        )
        if back:
            builder.add(
                InlineKeyboardButton(text=MenuKeyboard.back, callback_data="list_books")
            )

        builder.adjust(1)
        return builder.as_markup()

    @staticmethod
    def back_books_list_keyboard() -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.add(
            InlineKeyboardButton(text=MenuKeyboard.back, callback_data="list_books")
        )
        return builder.as_markup()

    @staticmethod
    def select_book_search_type() -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.button(
            text=BookSearchTypes.WORD_OR_PHRASE,
            callback_data=SelectBookSearchTypeCallbackFactory(
                search_type="word_or_phrase"
            ),
        )
        builder.button(
            text=BookSearchTypes.GENRE,
            callback_data=SelectBookSearchTypeCallbackFactory(search_type="genre"),
        )

        builder.adjust(1)
        return builder.as_markup()
