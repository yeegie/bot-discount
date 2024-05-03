from aiogram.fsm.state import State, StatesGroup


class CalculatePriceNumber(StatesGroup):
    value = State()


class CalculatePricePercent(StatesGroup):
    percent = State()
    value = State()

