import asyncio

from utils.db_api.add_commands import add_additive
from utils.db_api.database import create_db, db


async def add_additives():
    # await db.gino.drop_all()

    await add_additive(name="60",
                       category_name="Объем",
                       category_code="1_v",
                       price=1)
    await add_additive(name="100",
                       category_name="Объем",
                       category_code="1_v",
                       price=1)
    await add_additive(name="200",
                       category_name="Объем",
                       category_code="1_v",
                       price=1)
    await add_additive(name="300",
                       category_name="Объем",
                       category_code="1_v",
                       price=1)
    await add_additive(name="400",
                       category_name="Объем",
                       category_code="1_v",
                       price=1)
    await add_additive(name="500",
                       category_name="Объем",
                       category_code="1_v",
                       price=1)
    await add_additive(name="порция",
                       category_name="Объем",
                       category_code="1_v",
                       price=1)

    await add_additive(name="Коровье",
                       category_name="Молоко",
                       category_code="2_m",
                       price=1)
    await add_additive(name="Кокосовое",
                       category_name="Молоко",
                       category_code="2_m",
                       price=1)
    await add_additive(name="Соевое",
                       category_name="Молоко",
                       category_code="2_m",
                       price=1)
    await add_additive(name="Сливки",
                       category_name="Молоко",
                       category_code="2_m",
                       price=1)

    await add_additive(name="Сол. карамель",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Лесной орех",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Мятный",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Фисташка",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Карамель",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Кокос",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Попкорн",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Кленовый",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Ванильный",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Шок. печеньки",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Миндальный",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Айриш",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Макадамия",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)
    await add_additive(name="Малиновый",
                       category_name="Сироп",
                       category_code="3_s",
                       price=1)

    await add_additive(name="Мед",
                       category_name="Другое",
                       category_code="4_o",
                       price=1)
    await add_additive(name="Маршмеллоу",
                       category_name="Другое",
                       category_code="4_o",
                       price=1)


loop = asyncio.get_event_loop()
loop.run_until_complete(create_db())
loop.run_until_complete(add_additives())