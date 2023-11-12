
import logging
from aiogram import Bot
from aiogram import Dispatcher
from settings import settings

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=settings.bots.bot_token)
# Диспетчер
dp = Dispatcher()
