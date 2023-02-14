from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.STRINGS import ADMINS


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        member = await message.chat.get_member(message.from_user.id)
        return int(member) in ADMINS
