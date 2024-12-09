import asyncio
import random
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import dotenv_values

token = dotenv_values('.env')['BOT-TOKEN']
bot = Bot(token=token)
dp = Dispatcher()
router = Router()
dp.include_router(router)

NAME = ("Адина", "Тилек", "Лира", "Кира", "Фатима")

@router.message(Command("random_name"))
async def random_name(message: Message):
    random_choice = random.choice(NAME)
    await message.answer(f"Случайное имя: {random_choice}")

@router.message(Command("myinfo"))
async def myinfo(message: Message):
    user = message.from_user
    user_info = (
        f"Ваше ID: {user.id}\n"
        f"Ваше имя: {user.first_name}\n"
        f"Ваше имя пользователя: @{user.username if user.username else 'Нет'}"
    )
    await message.answer(user_info)

@router.message(Command("start"))
async def start_handler(message: Message):
    name = message.from_user.first_name
    await message.answer(f"Привет! {name} приветствует assistant_bot!")

async def main():
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
