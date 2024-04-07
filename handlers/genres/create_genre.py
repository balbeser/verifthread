from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from data.context import AddGenreText
from DatabaseAPI.commands import GenresAPI
from states import AddBookState, AddGenreState
from utils.create_book import create_book

router = Router()


@router.callback_query(AddBookState.genre, F.data == "add-custom-genre")
async def add_book(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.edit_text(AddGenreText.enter_custom_genre)
    await state.set_state(AddGenreState.name)


@router.message(StateFilter(AddGenreState.name))
async def enter_book_genre(message: Message, state: FSMContext) -> None:
    name = message.text

    if not (genre := await GenresAPI.select_genre(Name=name)):
        genre = await GenresAPI.add_genre(name=name)

    data = await state.get_data()
    await state.clear()

    await create_book(message=message, **data, genre_id=genre.Id)
