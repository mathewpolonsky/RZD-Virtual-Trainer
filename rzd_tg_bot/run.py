import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from config import TOKEN
from application.handlers import main_router
from application.test import test_router
from application.education import ed_router
from database.models import async_main


async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(main_router)
    dp.include_router(test_router)
    dp.include_router(ed_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
