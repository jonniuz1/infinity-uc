from aiogram import Dispatcher

from loader import dp
from .check_admin import IsAdmin


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    pass
