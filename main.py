import asyncio
import random
from aiogram import Bot, types, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import dotenv_values

from handlers.start import start_router
from handlers.dialog import dialog_router
from handlers.cafe import cafe_router
from handlers.reviews import questions_router
from handlers.admin_module import admin_module


token = dotenv_values('.env')['BOT-TOKEN']
bot = Bot(token=token)
dp = Dispatcher()
router = Router()
dp.include_router(router)

@dp.message(Command("img"))
async def img_handler(message: types.Message):
    photo = types.FSInputFile("img/koshechki.jpeg")
    await message.answer_photo(
        photo=photo,
        caption="кот!"
    )

async def main():
    dp.include_router(start_router)
    dp.include_router(dialog_router)
    dp.include_router(cafe_router)
    dp.include_router(questions_router)
    dp.include_router(admin_module)
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
