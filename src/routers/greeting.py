from aiogram import Router
from aiogram.types import Message
from aiogram.utils.markdown import hlink

from src.keyboards.inline.greeting_keyboard import greeting_keyboards

router = Router()


@router.message(commands=["start"])
async def greet_user(message: Message) -> None:
    text = [
        "Привет! Этот бот позволяет отправлять сообщения с различными текстовыми смайликами (kaomoji)",
        "",
        "Нажмите любую кнопку чтобы попробовать👇",
        "",
        "Примечание: Чтобы добавить эмодзи в начало, начните сообщение запятой (,)",
        "",
        f"Исходный код доступен на {hlink('Github', 'https://github.com/e1leet/kaomoji_bot')}",
    ]
    await message.answer("\n".join(text), reply_markup=greeting_keyboards)
