from aiogram.fsm.state import State, StatesGroup


class CalculatePriceNumber(StatesGroup):
    value = State()


class CalculatePricePercent(StatesGroup):
    percent = State()
    value = State()


class CalculateFixedPercent(StatesGroup):
    value = State()


class ChangePercent(StatesGroup):
    percent = State()
