from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menu import menu
from loader import dp
from utils.db_api import commands
from utils.db_api.database import db


@dp.message_handler(CommandStart())
async def start_message(message: types.Message):
    #await db.gino.drop_all()
    await commands.add_user(telegram_id=message.from_user.id,
                            name=message.from_user.full_name)

    await message.answer(f"Привет, {message.from_user.full_name.split()[0]}!\n"
                          "Sky Coffee☕ приветствует тебя!\n"
                         "У нас ЛУЧШИЙ кофе\n"
                         "в городе АХТУБИНСК!\n")

    await message.answer(text="Жми на кнопку МЕНЮ для заказа.", reply_markup=menu)


@dp.message_handler(commands="отзыв")
async def start_message(message: types.Message, state: FSMContext):
    await message.answer(f"Напиши свой отзыв")
    await state.set_state("review")

@dp.message_handler(state="review")
async def enter_review(message: types.Message, state: FSMContext):
    print(1)
    await commands.add_reviews(telegram_id=message.from_user.id,
                               name=message.from_user.full_name,
                               reviews=message.text)
    await state.finish()



