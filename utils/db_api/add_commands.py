from typing import List

from sqlalchemy import and_

from utils.db_api.models import Additives


async def add_additive(**kwargs):
    newadd = await Additives(**kwargs).create()
    return newadd


async def get_categories_add() -> List[Additives]:
    return await Additives.query.distinct(Additives.category_code).gino.all()

async def get_adds(category_code) -> List[Additives]:
    return await Additives.query.distinct(Additives.name).where(Additives.category_code == category_code).gino.all()

async def get_add(category_code, name) -> List[Additives]:
    add = await Additives.query.where(
        and_(Additives.category_code == category_code,
             Additives.name == name)
    ).gino.all()

    return add
#


# async def get_add(add_id) -> Additives:
#     add = await Additives.query.where(Additives.id == add_id).gino.first()
#
#     return add