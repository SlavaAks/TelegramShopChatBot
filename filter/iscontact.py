from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsTrueContact(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        try:
            return message.from_user.id == message.contact.user_id
        except:
            return False
