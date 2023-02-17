from aiogram import types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters.builtin import CommandStart

from data.STRINGS import ADMINS
from filters import IsAdmin, IsPrivate
from functions import send_to_alls
from keyboards.menu import menu_keyboard
from loader import dp, db


#
#
# @dp.message_handler(IsAdmin(), CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_keyboard)


@dp.message_handler(IsPrivate(), filters.Text(contains='set', ignore_case=True), user_id=ADMINS)
async def bot_start(message: types.Message):
    try:
        price = int(message.text[4:])
        await db.add_price_uc(price=price)
        await message.answer(f"Yangi narx o'rnatildi!\n"
                             f"Price UC = {price} UC")
    except:
        await message.reply("Xatolik yuz berdi!")


@dp.message_handler(IsPrivate(), filters.Text(contains='add_channel', ignore_case=True))
async def bot_start(message: types.Message):
    try:
        await db.add_channel(int(message.text[11:]))
        await message.reply("Qo'shildi!")
    except Exception as err:
        await message.reply(err)
        await message.reply("Kanal qo'shilmadi")


@dp.message_handler(IsPrivate(), text=['Kanalga', 'kanalga'], user_id=ADMINS, is_reply=True)
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


@dp.message_handler(IsPrivate(), text=['send', 'SEND', 'Send'], user_id=ADMINS, is_reply=True)
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


@dp.message_handler(IsPrivate(), IsAdmin(), text=['stat', 'Stat', 'STAT'])
async def stat(message: types.Message):
    count_all_users = await db.count_users()
    count_all_active_users = await db.count_active_users()
    await message.answer(f"Bot statistikasi:\n"
                         f"Barcha a'zolar: <b>{count_all_users}</b>\n"
                         f"Active a'zolar: <b>{count_all_active_users}</b>")
