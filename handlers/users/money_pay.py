import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink, hcode

from data.config import ADMINS
from keyboards.inline.basket_keyboards import paid_keyboard
from loader import dp
from utils.db_api.commands import select_user, update_user_basket, update_user_current_price
from utils.misc.qiwi import Payment, NoPaymentFound, NotEnoughMoney


@dp.message_handler(state="pay")
async def pay(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    user = await select_user(telegram_id)
    amount = user.current_price
    await update_user_basket(telegram_id, f"{user.basket}\n Покупатель заберет заказ: {message.text}\n\n"
                                          f"Всего оплачено: {amount}₽")

    payment = Payment(amount=amount)
    payment.create()

    await message.answer(
        "\n".join(
            [
                f"Для получения заказа перейдите по ссылке.",
                f"После завершения оплаты нажмите кнопку 'Оплатил'.",
                f"Всего к оплате: {amount}₽",
                "",
                hlink("Ссылка для оплаты", url=payment.invoice),
                "ID платежа:",
                hcode(payment.id)
            ]
        ),
        reply_markup=paid_keyboard
    )
    await state.set_state("qiwi")
    await state.update_data(payment=payment)


    @dp.callback_query_handler(text="cancel", state="qiwi")
    async def cancel_payment(callback: types.CallbackQuery, state: FSMContext):
        await callback.message.edit_text("Отменено")
        await state.finish()
        await callback.answer()

    @dp.callback_query_handler(text="paid", state="qiwi")
    async def approve_payment(callback: types.CallbackQuery, state: FSMContext):
        await callback.answer()
        data = await state.get_data()
        payment: Payment = data.get("payment")
        try:
            payment.check_payment()
        except NoPaymentFound:
            await callback.message.answer("Транзакция не найдена.")
            return
        except NotEnoughMoney:
            await callback.message.answer("Оплаченная сумма меньше необходимой.")
            return

        else:
            await callback.message.answer("Успешно оплачено")
            telegram_id = callback.from_user.id
            user = await select_user(telegram_id)
            for admin in ADMINS:
                try:
                    await dp.bot.send_message(admin, user.basket)
                except Exception as err:
                    logging.exception(err)

        await callback.message.edit_reply_markup()
        await state.finish()

        await update_user_basket(telegram_id, "")
        await update_user_current_price(telegram_id, 0)
        await callback.answer()

