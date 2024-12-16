import random
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message


dialog_router = Router()

NAME = ("Адина", "Тилек", "Лира", "Кира", "Фатима")

@dialog_router.message(Command("random_name"))
async def random_name(message: Message):
    random_choice = random.choice(NAME)
    await message.answer(f"Случайное имя: {random_choice}")


@dialog_router.message(Command("myinfo"))
async def myinfo(message: Message):
    user = message.from_user
    user_info = (
        f"Ваше ID: {user.id}\n"
        f"Ваше имя: {user.first_name}\n"
        f"Ваше имя пользователя: @{user.username if user.username else 'Нет'}"
    )
    await message.answer(user_info)