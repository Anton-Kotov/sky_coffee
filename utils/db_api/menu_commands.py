from typing import List

from sqlalchemy import and_

from utils.db_api.database import db
from utils.db_api.models import Item


async def add_item(**kwargs):
    newitem = await Item(**kwargs).create()
    return newitem

async def get_main() -> List[Item]:
    return await Item.query.distinct(Item.main_code).gino.all()

async def get_categories(main) -> List[Item]:
    return await Item.query.distinct(Item.category_code).where(Item.main_code == main).gino.all()

async def get_subcategories(category) -> List[Item]:
    return await Item.query.distinct(Item.subcategory_code).where(Item.category_code == category).gino.all()

async def count_items(main_code, category_code=None, subcategory_code=None):
    conditions = [Item.main_code == main_code]

    if category_code:
        conditions.append(Item.category_code == category_code)

    if subcategory_code:
        conditions.append(Item.subcategory_code == subcategory_code)

    total = await db.select([db.func.count()]).where(
        and_(*conditions)
    ).gino.scalar()

    return total

async def get_item(main_code, category_code, subcategory_code) -> List[Item]:
    item = await Item.query.where(
        and_(Item.main_code == main_code,
            Item.category_code == category_code,
             Item.subcategory_code == subcategory_code)
    ).gino.all()

    return item

# async def get_item(item_id) -> Item:
#     item = await Item.query.where(Item.id == item_id).gino.first()
#
#     return item
