from aiogram.filters.callback_data import CallbackData


class SelectGenreCallbackFactory(CallbackData, prefix="select-genre"):
    GenreId: int


class SelectGenreSearchFilterCallbackFactory(
    CallbackData, prefix="select-genre-filter"
):
    GenreId: int
