from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

cafe_router = Router()

@cafe_router.message(Command("cafe"))
async def cafe(message: Message):
    name = message.from_user.first_name

    ckb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="меню", callback_data="menu")]
        ]
    )
    await message.answer(f"Привет, {name}! Добро пожаловать в кафе.", reply_markup=ckb)

@cafe_router.callback_query(lambda c: c.data == "menu")
async def show_menu(callback_query: CallbackQuery):
    menu_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Напитки', callback_data="drinks")],
            [InlineKeyboardButton(text='Десерты', callback_data="desserts")],
        ]
    )

    await callback_query.message.answer("Выберите категорию:", reply_markup=menu_buttons)
    await callback_query.answer()

@cafe_router.callback_query(F.data == "drinks")
async def show_drinks(callback_query: CallbackQuery):
    print(callback_query.data)
    await callback_query.answer()
    await callback_query.message.answer("Coca-cola, Pepsi, Sprite, Fanta")

@cafe_router.callback_query(F.data == "desserts")
async def show_desserts(callback_query: CallbackQuery):
    print(callback_query.data)
    await callback_query.answer()
    await callback_query.message.answer("сан-себастьан, королевский, трюфель.")
