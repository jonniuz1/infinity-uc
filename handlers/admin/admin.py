from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove

from filters import IsAdmin
from keyboards.menu import menu_keyboard
from loader import dp


@dp.message_handler(IsAdmin(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_keyboard)

