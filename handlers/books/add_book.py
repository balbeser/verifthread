from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.types import ReplyKeyboardRemove as remove_keyboard

from utils.callback_factories.genres import SelectGenreCallbackFactory
from data.context import AddBookExceptions, AddBookText, MenuKeyboard
from DatabaseAPI.commands import BooksAPI, GenresAPI
from keyboards.inline.genres import GenresInlineKeyboards
from keyboards.reply.menu import ReplyMenuKeyboards
from states import AddBookState
from utils.create_book import create_book

router = Router()


@router.message(F.text == MenuKeyboard.add_book)
async def enter_book_name(message: Message, state: FSMContext) -> None:
    await message.answer(
        AddBookText.enter_book_name,
        reply_markup=remove_keyboard(),
    )

    await state.set_state(AddBookState.name)


@router.message(AddBookState.name)
async def enter_book_author(message: Message, state: FSMContext) -> None:
    name = message.text
    if await BooksAPI.select_book(Name=name):
        return await message.answer(
            AddBookExceptions.error_book_alredy_exists,
            reply_markup=ReplyMenuKeyboards.get_main_menu_markup(),
        )

    await message.answer(AddBookText.enter_book_author)

    await state.update_data(name=message.text)
    await state.set_state(AddBookState.author)


@router.message(AddBookState.author)
async def enter_book_desc(message: Message, state: FSMContext) -> None:
    await message.answer(AddBookText.enter_book_description)

    await state.update_data(author=message.text)
    await state.set_state(AddBookState.description)


@router.message(AddBookState.description)
async def enter_book_genre(message: Message, state: FSMContext) -> None:
    genres = await GenresAPI.select_genres()

    await message.answer(
        AddBookText.select_genre_or_create_new,
        reply_markup=GenresInlineKeyboards.add_book_select_genre_keyboard(
            genres=genres
        ),
    )

    await state.update_data(description=message.text)
    await state.set_state(AddBookState.genre)


@router.callback_query(AddBookState.genre, SelectGenreCallbackFactory.filter())
async def add_book(
    call: CallbackQuery, state: FSMContext, callback_data: SelectGenreCallbackFactory
) -> None:
    data = await state.get_data()
    await state.clear()
    await call.message.delete()

    await create_book(message=call.message, **data, genre_id=callback_data.GenreId)
