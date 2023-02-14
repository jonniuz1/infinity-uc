from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.STRINGS import WELCOME_TEXT
from keyboards.menu import menu_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(WELCOME_TEXT.format(message.from_user.first_name),
                         reply_markup=menu_keyboard)
