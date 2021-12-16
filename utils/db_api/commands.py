from datetime import datetime

from asyncpg import UniqueViolationError

from utils.db_api.database import db
from utils.db_api.models import User, Reviews


async def add_user(telegram_id: int, name: str, phone: str = None, basket: str = "",
                   current_price: float = 0, total_spent: float = 0):
    try:
        user = User(telegram_id=telegram_id, name=name, phone=phone, basket=basket, current_price=current_price, total_spent=total_spent)
        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(telegram_id: int):
    user = await User.query.where(User.telegram_id == telegram_id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.telegram_id).gino.scalar()
    return total


async def update_user_phone(telegram_id, email):
    user = await User.get(telegram_id)
    await user.update(email=email).apply()

async def update_user_basket(telegram_id: int, order: str):
    user = await User.get(telegram_id)
    await user.update(basket=order).apply()

async def update_user_current_price(telegram_id, current_price):
    user = await User.get(telegram_id)
    await user.update(current_price=current_price).apply()

async def update_total_spent(telegram_id, total_spent):
    user = await User.get(telegram_id)
    await user.update(total_spent=total_spent).apply()

async def add_reviews(telegram_id: int, name: str, reviews: str):
    reviews = Reviews(telegram_id=telegram_id, name=name, reviews=reviews)
    await reviews.create()




