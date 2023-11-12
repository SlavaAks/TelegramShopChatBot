from aiogram import types
from create_bot import dp
from keybords.start_button import reply_keyboard
from aiogram.filters.command import Command
# @dp.message(Command("start"))
async def cmd_start(message: types.Message):
    print("start")
    await message.answer(f'Здравствуй,{message.from_user.first_name}! Вы можете посмотреть товар в каталоге!', reply_markup=reply_keyboard)

# @dp.message(Command("contacts"))
async def cmd_contacts(message: types.Message):
   pass
