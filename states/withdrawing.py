from aiogram.dispatcher.filters.state import State, StatesGroup


class Pubg(StatesGroup):
    amount_uc = State()
    acc_id = State()
