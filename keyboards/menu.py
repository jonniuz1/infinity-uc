from aiogram.types import ReplyKeyboardMarkup

from data.STRINGS import MENU_REF_BUTTON, MENU_ADDRESS_BUTTON, MENU_INSTRUCT_BUTTON, MENU_CABINET_BUTTON

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.row(MENU_REF_BUTTON)
menu_keyboard.add(MENU_CABINET_BUTTON)
menu_keyboard.add(MENU_ADDRESS_BUTTON, MENU_INSTRUCT_BUTTON)