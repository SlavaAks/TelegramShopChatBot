import asyncio

from handlers import client
from create_bot import bot, dp
from aiogram.filters import Command
from aiogram import F




async def start_bot():
    client.register_handlers_client(dp)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start_bot())
