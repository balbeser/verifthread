from aiogram.fsm.state import StatesGroup, State


class AddBookState(StatesGroup):
    name = State()
    author = State()
    description = State()
    genre = State()


class SearchState(StatesGroup):
    keyword = State()
