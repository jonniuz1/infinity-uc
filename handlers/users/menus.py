from aiogram import types
from aiogram.dispatcher import FSMContext

from data.STRINGS import MENU_REF_BUTTON, MENU_REF_TEXT, MENU_CABINET_BUTTON, MENU_CABINET_TEXT, \
    CALLBACK_CABINET, MENU_INSTRUCT_BUTTON, MENU_INSTRUCT_TEXT, CALLBACK_WITHDRAW, MENU_WITHDRAW_TEXT, \
    CALLBACK_CHANNEL_ARROVED, CALLBACK_CHANNEL_DISAPPROVED, ADMINS, LINK_USER, CHANNEL, BEFORE_PAYMENT_TEXT_TO_ADMIN, \
    MENU_STAT_BUTTON, MENU_STAT_TEXT, CALLBACK_TOP_REFERRALS, CALLBACK_TOP_WITHDRAWERS, MENU_30UC, MENU_60UC, MENU_90UC, \
    MENU_120UC, MENU_180UC
from filters import IsPrivate
from keyboards.menu import keyboard_cancel, menu_keyboard, uc_menu
from loader import dp, db

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from data.STRINGS import REF_LINK
from states.withdrawing import Pubg

users_id = []


async def get_balance(user_id):
    withdrawed_uc = await db.get_withdrawed_uc_by_id(user_id)
    PRICE_UC = await db.get_price_uc()
    invites_count = await db.get_invites_count_by_id(user_id)
    balance = invites_count * PRICE_UC - withdrawed_uc
    return balance


@dp.message_handler(IsPrivate(), text=MENU_REF_BUTTON)
async def ref_link(message: types.Message):
    user_id = message.from_user.id
    price = await db.get_price_uc()
    inline_ref_link = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ulashish",
                                     url="https://t.me/share/url?url=" + REF_LINK.format(user_id)),
            ]
        ]
    )

    await message.answer(MENU_REF_TEXT.format(user_id, price), reply_markup=inline_ref_link)


@dp.message_handler(IsPrivate(), text=MENU_CABINET_BUTTON)
async def cabinet(message: types.Message):
    user_id = message.from_user.id
    withdrawed_uc = await db.get_withdrawed_uc_by_id(user_id)
    invites_count = await db.get_invites_count_by_id(user_id)
    balance = await get_balance(user_id)
    inline_cabinet = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Yechib olish",
                                     callback_data=CALLBACK_CABINET),
            ]
        ]
    )

    await message.answer(MENU_CABINET_TEXT.format(user_id, balance, invites_count, withdrawed_uc),
                         reply_markup=inline_cabinet)


@dp.callback_query_handler(text=CALLBACK_CABINET)
async def withdraw(query: types.CallbackQuery):
    if await get_balance(query.from_user.id) >= 30:
        inline_withdraw = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('PUBG Mobile', callback_data=CALLBACK_WITHDRAW)
                ]
            ]
        )
        await query.bot.delete_message(query.from_user.id, query.message.message_id)
        await query.bot.send_message(query.from_user.id, MENU_WITHDRAW_TEXT, reply_markup=inline_withdraw)
    else:
        await query.answer("Hisobingizda yetarli UC mavjud emas!\nEng kam yechib olish miqdori 30 UC", True)
        await query.bot.delete_message(query.from_user.id, query.message.message_id)


@dp.callback_query_handler(text=CALLBACK_WITHDRAW)
async def withdraw(query: types.CallbackQuery):
    await query.bot.delete_message(query.from_user.id, query.message.message_id)
    await dp.bot.send_message(query.from_user.id, 'Yetarli UC miqdorini tanlang:', reply_markup=uc_menu)
    await Pubg.amount_uc.set()


@dp.message_handler(IsPrivate(), text="🔙 Orqaga", state=Pubg.amount_uc)
async def cancel(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.reply("Siz bosh sahifadasiz!", reply_markup=menu_keyboard)


@dp.message_handler(IsPrivate(), commands=["start"], state=Pubg.amount_uc)
async def cancel(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.reply("Siz bosh sahifadasiz!", reply_markup=menu_keyboard)


@dp.message_handler(IsPrivate(), text=[MENU_30UC, MENU_60UC, MENU_90UC, MENU_120UC, MENU_180UC], state=Pubg.amount_uc)
async def withdraw(message: types.Message, state: FSMContext):
    amount = message.text[:-3]
    await state.update_data({
        "amount": amount
    })
    await dp.bot.send_message(message.from_user.id,
                              f'!!! <b>Iltimos</b> !!!\n Pubg akkount id raqamini to\'g\'ri kiriting: ',
                              reply_markup=ReplyKeyboardRemove())
    await Pubg.acc_id.set()


@dp.message_handler(IsPrivate(), state=Pubg.acc_id)
async def withdraw(message: types.Message, state=FSMContext):
    try:
        acc_id = int(message.text)
        await dp.bot.send_message(message.from_user.id, "So'rov yuborildi!")
        users_id.append(message.from_user.id)
        await dp.bot.delete_message(message.from_user.id, message.message_id)
        data = await state.get_data()
        amount = data.get('amount')
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
        await dp.bot.send_message(CHANNEL[0],
                                  BEFORE_PAYMENT_TEXT_TO_ADMIN.format(acc_id, message.from_user.id,
                                                                      message.from_user.first_name,
                                                                      amount), reply_markup=inline_channel)
        await message.answer("Admin to'lovni tasdiqlashini kuting!", reply_markup=menu_keyboard)
        await state.finish()
    except:
        if message.text == "🔙 Orqaga":
            await message.reply("Siz yana bosh menudasiz!", reply_markup=menu_keyboard)
            await state.reset_state()
        else:
            await message.reply("To'g'ri id kiriting!!!", reply_markup=keyboard_cancel)
            return


@dp.callback_query_handler(text=CALLBACK_CHANNEL_ARROVED)
async def withdraw(query: types.CallbackQuery):
    user_id = query.from_user.id
    withdrawable_uc = int(query.message.text[-36:-32])
    if query.from_user.id in ADMINS:
        await query.bot.delete_message(CHANNEL[0], query.message.message_id)
        await query.bot.send_message(CHANNEL[0],
                                     f'<a href="{LINK_USER}{users_id[-1]}">{users_id[-1]}</a> ga {withdrawable_uc} Uc to\'landi!')
        try:
            await query.bot.send_message(users_id[-1], f"{withdrawable_uc} Uc to'landi!")
            await db.update_withdrawed_uc(users_id[-1], withdrawable_uc)
            users_id.clear()
        except Exception:
            await dp.bot.send_message(ADMINS[0], "Xatolik yuz berdi!")
    else:
        await query.answer(text="Bu tugma siz uchun emas!", show_alert=True)


@dp.callback_query_handler(text=CALLBACK_CHANNEL_DISAPPROVED)
async def withdraw(query: types.CallbackQuery):
    if query.from_user.id in ADMINS:
        await query.bot.delete_message(CHANNEL[0], query.message.message_id)
        await query.bot.send_message(query.from_user.id, "Uc to'lash rad etildi! Boshqatan urinib ko'ring!")
    else:
        await query.answer(text="Bu tugma siz uchun emas!", show_alert=True)


@dp.message_handler(IsPrivate(), text=MENU_INSTRUCT_BUTTON)
async def cabinet(message: types.Message):
    price = await db.get_price_uc()
    await message.answer(MENU_INSTRUCT_TEXT.format(price))


@dp.message_handler(IsPrivate(), text=MENU_STAT_BUTTON)
async def stat(message: types.Message):
    inline_stat = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Top referrallar", callback_data=CALLBACK_TOP_REFERRALS),
                InlineKeyboardButton(text="Top Uc yechganlar", callback_data=CALLBACK_TOP_WITHDRAWERS)
            ]
        ]
    )
    await message.reply(MENU_WITHDRAW_TEXT, reply_markup=inline_stat)


@dp.callback_query_handler(text=CALLBACK_TOP_REFERRALS)
async def stat(query: types.CallbackQuery):
    f_text = '' + MENU_STAT_TEXT
    top_referals = await db.select_top_referals()
    for chat_id, count in top_referals:
        f_text += str(chat_id) + ' ----- ' + str(count) + "\n"
    await dp.bot.delete_message(query.from_user.id, query.message.message_id)
    await dp.bot.send_message(query.from_user.id, f_text)


@dp.callback_query_handler(text=CALLBACK_TOP_WITHDRAWERS)
async def stat(query: types.CallbackQuery):
    f_text = 'Eng ko\'p UC yechib olganlar:\n'
    top_withdrawers = await db.select_top_withdrawers()
    for chat_id, count in top_withdrawers:
        f_text += str(chat_id) + ' ----- ' + str(count) + "\n"
    await dp.bot.delete_message(query.from_user.id, query.message.message_id)
    await dp.bot.send_message(query.from_user.id, f_text)
