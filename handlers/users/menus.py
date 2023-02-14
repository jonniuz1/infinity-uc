from aiogram import types

from data.STRINGS import MENU_REF_BUTTON, MENU_REF_TEXT, MENU_CABINET_BUTTON, MENU_CABINET_TEXT, \
    CALLBACK_CABINET, MENU_INSTRUCT_BUTTON, MENU_INSTRUCT_TEXT, CALLBACK_WITHDRAW, MENU_WITHDRAW_TEXT, \
    CALLBACK_CHANNEL_ARROVED, CALLBACK_CHANNEL_DISAPPROVED, ADMINS, LINK_USER
from loader import dp

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from data.STRINGS import REF_LINK

users_id = []

@dp.message_handler(text=MENU_REF_BUTTON)
async def ref_link(message: types.Message):
    user_id = message.from_user.id
    inline_ref_link = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ulashish",
                                     url="https://t.me/share/url?url=" + REF_LINK.format(user_id)),
            ]
        ]
    )

    await message.answer(MENU_REF_TEXT.format(user_id), reply_markup=inline_ref_link)


@dp.message_handler(text=MENU_CABINET_BUTTON)
async def cabinet(message: types.Message):
    user_id = message.from_user.id

    inline_cabinet = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Yechib olish",
                                     callback_data=CALLBACK_CABINET),
            ]
        ]
    )

    await message.answer(MENU_CABINET_TEXT.format(user_id, 25, 3, 2), reply_markup=inline_cabinet)


@dp.message_handler(text=CALLBACK_CABINET)
async def withdraw(message: types.Message):
    inline_withdraw = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('PUBG Mobile', callback_data=CALLBACK_WITHDRAW)
            ]
        ]
    )
    await message.bot.delete_message(message.from_user.id, message.message_id)
    await message.bot.send_message(message.from_user.id, MENU_WITHDRAW_TEXT, reply_markup=inline_withdraw)


@dp.callback_query_handler(text=CALLBACK_CABINET)
async def withdraw(query: types.CallbackQuery):
    inline_withdraw = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('PUBG Mobile', callback_data=CALLBACK_WITHDRAW)
            ]
        ]
    )
    await query.bot.delete_message(query.from_user.id, query.message.message_id)
    await query.bot.send_message(query.from_user.id, MENU_WITHDRAW_TEXT, reply_markup=inline_withdraw)


@dp.message_handler(text=MENU_INSTRUCT_BUTTON)
async def cabinet(message: types.Message):
    await message.answer(MENU_INSTRUCT_TEXT)


@dp.callback_query_handler(text=CALLBACK_WITHDRAW)
async def withdraw(query: types.CallbackQuery):
    await query.bot.send_message(query.from_user.id, "So'rov yuborildi!")
    users_id.append(query.from_user.id)
    await query.bot.delete_message(query.from_user.id, query.message.message_id)
    inline_channel = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="To'landi!", callback_data=CALLBACK_CHANNEL_ARROVED)
            ],
            [
                InlineKeyboardButton(text="Rad etildi!", callback_data=CALLBACK_CHANNEL_DISAPPROVED)
            ],

        ]
    )
    await query.bot.send_message(-1001551015352, "Ishladi!", reply_markup=inline_channel)
    await query.answer("Hammasi tayyor!", True)


@dp.callback_query_handler(text=CALLBACK_CHANNEL_ARROVED)
async def withdraw(query: types.CallbackQuery):
    if query.from_user.id in ADMINS:
        await query.bot.delete_message(-1001551015352, query.message.message_id)
        await query.bot.send_message(-1001551015352, f'<a href="{LINK_USER}{users_id[-1]}">{users_id[-1]}</a>ga Uc to\'landi!')
        try:
            await query.bot.send_message(users_id[-1], "Uc to'landi!", reply_markup=ReplyKeyboardRemove())
            users_id.clear()
        except Exception as err:
            print(err)
    else:
        await query.answer(text="Bu tugma siz uchun emas", show_alert=True)


@dp.callback_query_handler(text=CALLBACK_CHANNEL_DISAPPROVED)
async def withdraw(query: types.CallbackQuery):
    if query.from_user.id in ADMINS:
        await query.bot.delete_message(-1001551015352, query.message.message_id)
        await query.bot.send_message(query.from_user.id, "Uc to'lash rad etildi!", reply_markup=ReplyKeyboardRemove())
    else:
        await query.answer(text="Bu tugma siz uchun emas", show_alert=True)
