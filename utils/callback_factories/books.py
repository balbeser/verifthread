from typing import Annotated
from aiogram.filters.callback_data import CallbackData

from data.default_values import BookSearchTypes


class SelectBookCallbackFactory(CallbackData, prefix="select-book"):
    BookId: int
    back: bool


class DeleteBookCallbackFactory(CallbackData, prefix="delete-book"):
    BookId: int


class SelectBookSearchTypeCallbackFactory(CallbackData, prefix="search-book-type"):
    search_type: Annotated[str, BookSearchTypes]
