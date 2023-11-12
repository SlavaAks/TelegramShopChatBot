import asyncio

from handlers import client
from create_bot import bot, dp
from aiogram.filters import Command





async def start_bot():
    dp.message.register(client.cmd_start,Command(commands=['start']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start_bot())
