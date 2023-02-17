from aiogram.types import ReplyKeyboardMarkup

from data.STRINGS import MENU_REF_BUTTON, MENU_STAT_BUTTON, MENU_INSTRUCT_BUTTON, MENU_CABINET_BUTTON, MENU_30UC, \
    MENU_60UC, MENU_90UC, MENU_120UC, MENU_180UC

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.row(MENU_REF_BUTTON)
menu_keyboard.add(MENU_CABINET_BUTTON)
menu_keyboard.add(MENU_STAT_BUTTON, MENU_INSTRUCT_BUTTON)

keyboard_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_cancel.add("🔙 Orqaga")

uc_menu = ReplyKeyboardMarkup(resize_keyboard=True)
uc_menu.row(MENU_30UC, MENU_60UC)
uc_menu.add(MENU_90UC, MENU_120UC)
uc_menu.add(MENU_180UC, "🔙 Orqaga")
