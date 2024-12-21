from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

questions_router = Router()

class Questions(StatesGroup):
    phone_number = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

def get_rating_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="1 ⭐", callback_data="1"),
            InlineKeyboardButton(text="2 ⭐", callback_data="2"),
            InlineKeyboardButton(text="3 ⭐", callback_data="3"),
            InlineKeyboardButton(text="4 ⭐", callback_data="4"),
            InlineKeyboardButton(text="5 ⭐", callback_data="5"),
        ]
    ])

@questions_router.callback_query(F.data == 'review')
async def phone_number(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Как с вами можно связаться? (Напишите свои контактные данные)")
    await state.set_state(Questions.phone_number)

@questions_router.message(Questions.phone_number)
async def food_rating(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("Какую оценку поставите нашей кафейне?", reply_markup=get_rating_keyboard())
    await state.set_state(Questions.food_rating)

@questions_router.callback_query(Questions.food_rating)
async def cleanliness_rating(callback_query: types.CallbackQuery, state: FSMContext):
    food_rating = int(callback_query.data)
    await state.update_data(food_rating=food_rating)
    await callback_query.message.answer("Как оцениваете чистоту заведения?", reply_markup=get_rating_keyboard())
    await state.set_state(Questions.cleanliness_rating)

@questions_router.callback_query(Questions.cleanliness_rating)
async def extra_comments(callback_query: types.CallbackQuery, state: FSMContext):
    cleanliness_rating = int(callback_query.data)
    await state.update_data(cleanliness_rating=cleanliness_rating)
    await callback_query.message.answer("Дополнительные комментарии/жалобы? Напишите ваш отзыв.")
    await state.set_state(Questions.extra_comments)

@questions_router.message(Questions.extra_comments)
async def handle_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    data = await state.get_data()

    phone_number = data.get('phone_number', 'Не указано')
    food_rating = data.get('food_rating', 'Не указано')
    cleanliness_rating = data.get('cleanliness_rating', 'Не указано')
    extra_comments = data.get('extra_comments', 'Нет комментариев')

    await message.answer(
        f"Спасибо за ваш отзыв!\n"
        f"Способ связи: {phone_number}\n"
        f"Оценка еды: {food_rating}\n"
        f"Оценка чистоты: {cleanliness_rating}\n"
        f"Дополнительные комментарии: {extra_comments}"
    )
    await state.clear()
