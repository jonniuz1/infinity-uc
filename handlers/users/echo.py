from aiogram import types

from data.STRINGS import ADMINS
from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), user_id=ADMINS)
async def admin_help(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n "
                         f"Admin foydalanishi mumkin bo'lgan kommandalar:\n"
                         f"send - reklama jo'natish uchun\n"
                         f"stat - bot statistikasini ko'rish\n"
                         f"set [UC narxi] - yangi uc narx o'rnatish\n"
                         f"add_channel [kanal id] - post joylashtirish uchun kanal")


@dp.message_handler(IsPrivate())
async def bot(message: types.Message):
    await message.answer("💴")
