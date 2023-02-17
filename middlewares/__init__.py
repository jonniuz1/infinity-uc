from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .checksub import Check


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(Check())
#
# MENU_30UC = "30 Uc"
# MENU_60UC = "60 Uc"
# MENU_90UC = "90 Uc"
# MENU_120UC = "120 Uc"
# MENU_180UC = "180 Uc"
#
# BEFORE_PAYMENT_TEXT_TO_ADMIN = f"<code>{{}}</code>\n<a href='tg://user?id={{}}'>{{}}</a> {{}} UC chiqarish uchun so'rov berdi!"
# d = BEFORE_PAYMENT_TEXT_TO_ADMIN.format(123132132131, 123131321321, "JO", 145)

# print((int(MENU_120UC[:-2])))
# print(len(MENU_120UC[:-2]))
# print((int(d[-36:-32])))
# print(len(MENU_120UC[:-2]))