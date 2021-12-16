from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData



async def basket_select():
    markup = InlineKeyboardMarkup(row_width=2)

    drop = InlineKeyboardButton(text="Очистить корзину", callback_data="drop")
    markup.insert(drop)

    pay = InlineKeyboardButton(text="Перейти к оплате", callback_data="pay")
    markup.insert(pay)

    return markup

paid_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Оплатил",
                callback_data="paid")
        ],
        [
            InlineKeyboardButton(
                text="Отмена",
                callback_data="cancel")
        ],
    ]
)

async def time_select():
    markup = InlineKeyboardMarkup(row_width=3)

    now = InlineKeyboardButton(text="Сейчас", callback_data="now")
    markup.insert(now)

    hour = InlineKeyboardButton(text="Через час", callback_data="hour")
    markup.insert(hour)

    your_time = InlineKeyboardButton(text="Свой вариант", callback_data="your_time")
    markup.insert(your_time)

    return markup

# time_select = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text="Сейчас",
#                 callback_data="now")
#         ],
#         [
#             InlineKeyboardButton(
#                 text="В течении часа",
#                 callback_data="hour")
#         ],
# [
#             InlineKeyboardButton(
#                 text="Свой вариант",
#                 callback_data="your_time")
#         ]
#     ]
# )



