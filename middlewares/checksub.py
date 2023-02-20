from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from loader import db, bot
from utils.misc import subscription


class Check(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        CHANNELS = await db.select_all_channels()
        if update.message:
            if update.message.text.startswith("/start") and len(update.message.text.split()) == 2:
                return
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return
        final_status = True
        final_text = "Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling!\n"
        for channel in CHANNELS:
            chat = await bot.get_chat(chat_id=channel[0])
            status = await subscription.check(user_id=user,
                                              channel=chat['id'])
            final_status *= status

            if not status:
                invite_link = chat['invite_link']
                final_text += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

        if not final_status:
            await update.message.answer(final_text, disable_web_page_preview=True)
            raise CancelHandler()
