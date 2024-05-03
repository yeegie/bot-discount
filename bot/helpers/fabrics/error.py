from aiogram.filters.callback_data import CallbackData
from typing import Optional

class ErrorCallback(CallbackData, prefix='error'):
    action: str
    state_to: Optional[str]
    