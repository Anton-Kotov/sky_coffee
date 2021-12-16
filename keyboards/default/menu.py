from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="МЕНЮ📖"),
        ]
    ],
    resize_keyboard=True
)

basket = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="МЕНЮ📖"),
        ],
        [
            KeyboardButton(text="КОРЗИНА")
        ]
    ],
    resize_keyboard=True
)

