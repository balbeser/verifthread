from glob import glob
from importlib import import_module
from os.path import join

from aiogram import Dispatcher, Router
from loguru import logger

from data.default_values import Genres
from DatabaseAPI.commands import GenresAPI


class LoaderServices:
    @staticmethod
    async def load_modules(dp: Dispatcher) -> None:
        """
        Load modules from the 'handlers' directory and add the handlers to the dispatcher.

        Args:
            dp (Dispatcher): The aiogram Dispatcher object.
        """
        handlers_dir: str = "handlers"
        modules = [
            module.replace("/", ".").replace(".py", "")
            for module in map(
                lambda item: item.replace("\\", "/"),
                glob(join(handlers_dir, "**", "*.py"), recursive=True),
            )
        ]
        for module in modules:
            module_name = import_module(module)
            if hasattr(module_name, "router"):
                router: Router = getattr(module_name, "router")
                dp.include_router(router)
                logger.info(f"Success add handler {module}!")

    @staticmethod
    async def create_default_genres() -> None:
        """
        Genering default genres
        """
        if not await GenresAPI.select_genre(Id=1):
            for genre in Genres.genres_list:
                await GenresAPI.add_genre(name=genre)
