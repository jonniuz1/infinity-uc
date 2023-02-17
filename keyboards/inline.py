from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_check_sub = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="30 Uc", callback_data="30uc"),
            InlineKeyboardButton(text="60 Uc", callback_data="60uc")
        ],
        [
            InlineKeyboardButton(text="90 Uc", callback_data="90uc"),
            InlineKeyboardButton(text="120 Uc", callback_data="120uc")
        ],
        [
            InlineKeyboardButton(text="180 Uc", callback_data="180uc")
        ],
    ]
)
