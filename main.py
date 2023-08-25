import asyncio
import logging

from aiogram import Dispatcher, Bot
from handler import start, weather
from config import settings
from utils.commands import set_up_default_commands


# Настройка логирования
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=settings.TOKEN)
# Объект диспетчера
dp = Dispatcher()

dp.include_routers(
    start.router,
    weather.router,
)


async def main():
    await set_up_default_commands(bot)
    await dp.start_polling(bot)


# Запуск скрипта
if __name__ == '__main__':
    asyncio.run(main())
