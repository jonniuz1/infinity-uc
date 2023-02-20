import asyncio
import logging

from aiogram.utils import exceptions

from data.STRINGS import ADMINS
from loader import db

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('broadcast')


#
# def get_chats():
#     """
#     Return users list
#     """
#     yield from Chats.Users()


async def send_message(user_id: int, msg) -> bool:
    try:
        await msg.copy_to(chat_id=user_id, reply_markup=msg.reply_markup)
    except exceptions.BotBlocked:
        pass
    except exceptions.ChatNotFound:
        pass
    except exceptions.RetryAfter as e:
        await asyncio.sleep(e.timeout)
        await msg.copy_to(chat_id=user_id, reply_markup=msg.reply_markup)
    except exceptions.UserDeactivated:
        pass
    except exceptions.MigrateToChat as e:
        try:
            await msg.copy_to(chat_id=e.migrate_to_chat_id, reply_markup=msg.reply_markup)
        except:
            pass
    except exceptions.TelegramAPIError:
        pass
    else:
        pass
        return True
    return False


async def broadcaster(msg) -> str:
    """
    Simple broadcaster
    :return: Count of messages
    """
    sends = 0
    error_sends = 0
    try:
        for user_id in await db.select_all_users():
            if not user_id[0] in ADMINS:
                if await send_message(user_id=user_id[0], msg=msg):
                    sends += 1
                else:
                    error_sends += 1
                    await db.set_active(user_id[0], False)
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    except Exception as err:
        return "Jo'natishda xatolik yuz berdi!"

    return f"Yuborildi: {sends}\nYuborilmadi: {error_sends}"


async def channel_broadcaster(msg) -> str:
    """
    Simple broadcaster
    :return: Count of messages
    """
    sends = 0
    error_sends = 0
    try:
        for channel in await db.select_all_channels():
            if await send_message(user_id=channel[0], msg=msg):
                sends += 1
            else:
                error_sends += 1
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    except Exception as err:
        return "Jo'natishda xatolik yuz berdi!"

    return f"Yuborildi: {sends}\nYuborilmadi: {error_sends}"
