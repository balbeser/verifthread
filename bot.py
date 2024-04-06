from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger

from config.config import Config, load_config
from DatabaseAPI.database import create_base
from utils.loader import LoaderServices


# Функция конфигурации и запуска бота
async def main() -> None:
    logger.info("Starting bot")

    # Создаем кофниг
    config: Config = load_config()

    # Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
    storge: MemoryStorage = MemoryStorage()

    # Создаем таблицы базы данных
    await create_base()

    # Создаем стандартные жанры
    await LoaderServices.create_default_genres()

    # Создаем объекты бота и диспетчера
    default_properties = DefaultBotProperties(parse_mode=None)

    bot: Bot = Bot(token=config.Bot.token, default=default_properties)
    dp: Dispatcher = Dispatcher(storage=storge)

    # Регистрируем хендлеры
    await LoaderServices.load_modules(dp=dp)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        run(main=main())
    except KeyboardInterrupt:
        logger.info("Stopped bot.")
