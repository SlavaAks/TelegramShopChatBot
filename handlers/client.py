from aiogram import Dispatcher, types, F
from aiogram.filters import Command

from keybords.start_button import reply_keyboard
# @dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f'Здравствуй,{message.from_user.first_name}! Вы можете посмотреть товар в каталоге!', reply_markup=reply_keyboard)

# @dp.message(Command("contacts"))
async def cmd_contacts(message: types.Message):
   await message.answer(f'Связаться с администратором \n телефон:+375295044322 (МТС) \n телеграм:@slava8aks  ')


def register_handlers_client(dp:Dispatcher):
    dp.message.register(cmd_start, Command(commands=['start']))
    dp.message.register(cmd_contacts, F.text == 'Контакты')