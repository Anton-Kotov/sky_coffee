from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.basket_keyboards import basket_select
from keyboards.inline.menu_keyboards import basket_add_cd
from loader import dp
from utils.db_api.commands import update_user_basket, select_user, update_user_current_price, update_total_spent


@dp.callback_query_handler(basket_add_cd.filter())
async def add_basket(callback: types.CallbackQuery, state: FSMContext):

    telegram_id = callback.from_user.id
    user = await select_user(telegram_id)
    data = await state.get_data()
    order = data["order"] + user.basket
    current_price = data["price"] + user.current_price

    await update_user_basket(telegram_id, order)
    await update_user_current_price(telegram_id, current_price)
    await callback.answer()

@dp.message_handler(text="КОРЗИНА")
async def show_basket(message: types.Message, state: FSMContext):
    markup = await basket_select()
    telegram_id = message.from_user.id
    user = await select_user(telegram_id)
    text = f"{user.basket}\n\nВсего к оплате {user.current_price}₽"
    await message.answer(text, reply_markup=markup)


@dp.callback_query_handler(text="drop")
async def drop_basket(callback: types.CallbackQuery, state: FSMContext):

    telegram_id = callback.from_user.id
    await update_user_basket(telegram_id, "")
    await update_user_current_price(telegram_id, 0)
    await state.finish()
    await callback.answer(text="Корзина очищена", show_alert=True)

@dp.callback_query_handler(text="pay")
async def pay_basket(callback: types.CallbackQuery, state: FSMContext):
    telegram_id = callback.from_user.id
    user = await select_user(telegram_id)
    total_spent = user.total_spent
    amount = user.current_price
    await update_total_spent(telegram_id, total_spent=total_spent + amount)

    await callback.message.answer(text="Напишите, когда хотите забрать заказ?\n"
                                       "(СЕЙЧАС или укажите точное время)")
    await state.set_state("pay")
    await callback.answer()

