import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from main.handlers.main_handlers import main_handlers
from main.settings import settings


async def main() -> None:
    bot = Bot(token=settings.TG_TOKEN)
    dp = Dispatcher()
    dp.include_routers(main_handlers)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
