from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import CommandStart

from data.STRINGS import ADMINS
from filters import IsAdmin
from functions import send_to_alls
from keyboards.menu import menu_keyboard
from loader import dp, db


@dp.message_handler(IsAdmin(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_keyboard)


@dp.message_handler(filters.Text(contains='add_channel', ignore_case=True))
async def bot_start(message: types.Message):
    try:
        await db.add_channel(int(message.text[11:]))
        await message.reply("Qo'shildi!")
    except Exception as err:
        await message.reply(err)
        await message.reply("Kanal qo'shilmadi")


@dp.message_handler(text=['Kanalga', 'kanalga'], user_id=ADMINS, is_reply=True)
async def admin(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.add(
        types.InlineKeyboardButton('Kanalga yuborish', callback_data='send-channel'),
    )
    await message.reply_to_message.reply("Barchasi to'g'ri bo'lsa yuborish tugmasini bosing",
                                         reply_markup=keyboard_markup)


@dp.callback_query_handler(user_id=ADMINS, text=['send-channel'])
async def answer_call(query: types.CallbackQuery):
    await query.message.edit_text("Yuborilmoqda...")
    send_wait = await send_to_alls.channel_broadcaster(query.message.reply_to_message)
    await query.message.edit_text(str(send_wait))


@dp.message_handler(text=['send', 'SEND', 'Send'], user_id=ADMINS, is_reply=True)
async def admin(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.add(
        types.InlineKeyboardButton('Yuborish', callback_data='send-all'),
    )
    await message.reply_to_message.reply("Barchasi to'g'ri bo'lsa yuborish tugmasini bosing",
                                         reply_markup=keyboard_markup)


@dp.callback_query_handler(user_id=ADMINS, text=['send-all'])
async def answer_call(query: types.CallbackQuery):
    await query.message.edit_text("Yuborilmoqda...")
    send_wait = await send_to_alls.broadcaster(query.message.reply_to_message)
    await query.message.edit_text(str(send_wait))


@dp.message_handler(IsAdmin(), text=['stat', 'Stat', 'STAT'])
async def stat(message: types.Message):
    await message.answer(f"Stat")


@dp.message_handler(IsAdmin())
async def admin_help(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n "
                         f"Admin foydalanishi mumkin bo'lgan kommandalar:\n"
                         f"send - reklama jo'natish uchun\n"
                         f"stat - bot statistikasini ko'rish")
