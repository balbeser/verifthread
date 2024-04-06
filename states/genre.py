from aiogram.fsm.state import StatesGroup, State


class AddGenreState(StatesGroup):
    name = State()
