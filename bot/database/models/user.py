from tortoise import Model, fields
from .dataclasses import UserType


class User(Model):
    id = fields.IntField(pk=True)

    type = fields.CharField(max_length=32, default=UserType.user, validators=[UserType.validator])

    user_id = fields.BigIntField(unique=True)
    full_name = fields.CharField(max_length=130)
    username = fields.CharField(max_length=32, null=True)
    language = fields.CharField(max_length=2, default='ru')

    register_time = fields.DatetimeField(auto_now_add=True)

    fixed_percent = fields.FloatField(default=0)

    class Meta:
        table = 'users'

    @property
    def is_admin(self):
        return self.type == 'admin'
