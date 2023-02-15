import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.STRINGS import WELCOME_TEXT, ADMINS
from keyboards.menu import menu_keyboard
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if len(message.text.split()) == 2:
        referral = int(message.text.split()[1])
        await db.update_invites_count(referral)
    else:
        referral = 0
    try:
        user = await db.add_user(
            chat_id=message.from_user.id,
            username=message.from_user.username,
            active=True,
            referral=referral,
            count_referrals=0
        )

        # ADMINGA xabar beramiz
        msg = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> bazaga qo'shildi."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
        await message.answer("Botimizga xush kelibsiz!")
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(chat_id=message.from_user.id)
        await db.set_active(user[0], True)
        await message.answer("Sizni yana ko'rganimdan xursandman!")

    await message.answer(WELCOME_TEXT.format(message.from_user.first_name),
                         reply_markup=menu_keyboard)
