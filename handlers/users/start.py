import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.STRINGS import WELCOME_TEXT, ADMINS, BOT_LINK, BOT_NAME
from filters import IsPrivate
from keyboards.menu import menu_keyboard
from loader import dp, db, bot
from utils.misc import subscription



@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    if len(message.text.split()) == 2:
        if await db.is_exist_user(int(message.text.split()[-1])):
            referral = int(message.text.split()[1])
            await db.update_invites_count(referral)
            msg = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> sizning havolangiz orqali botga a'zo bo'ldi!."
            await bot.send_message(chat_id=referral, text=msg)
        else:
            referral = 0
    else:
        referral = 0
    try:
        user = await db.add_user(
            chat_id=message.from_user.id,
            username=message.from_user.username,
            active=True,
            withdrawed_uc=0,
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


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    CHANNELS = await db.select_all_channels()
    channels = []
    channel_text = str()
    for channel in CHANNELS:
        chat = await dp.bot.get_chat(chat_id=channel[0])
        status = await subscription.check(user_id=message.from_user.id,
                                          channel=chat['id'])
        if not status:
            invite_link = chat['invite_link']
            channel_text += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"
    await message.reply(f'Botdan foydalanish uchun <a href="{BOT_LINK}">{BOT_NAME}</a> ga bosing!\n'
                        f'{channel_text} !!!')
