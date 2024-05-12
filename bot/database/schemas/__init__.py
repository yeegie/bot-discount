from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserSchema:
    id: int
    type: str
    user_id: int
    full_name: str
    username: str
    language: str
    register_time: datetime
    fixed_percent: float
