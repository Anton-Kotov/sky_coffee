from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.add_commands import get_categories_add, get_add, get_adds
from utils.db_api.menu_commands import get_categories, count_items, get_subcategories, get_item, get_main, get_item

# menu_cd = CallbackData("show_menu", "level", "main", "category", "subcategory", "item_id")

menu_cd = CallbackData("sm", "level", "main", "category", "subcategory",
                           "main_add", "category_add", "name")

basket_add_cd = CallbackData("basket", "add")


# def make_callback_data(level, main="0", category="0", subcategory="0", item_id="0"):
#
#     return menu_cd.new(level=level, main=main, category=category, subcategory=subcategory, item_id=item_id)

def make_callback_data(level, main="0", category="0", subcategory="0",
                           main_add="0", category_add="0", name="0"):

    return menu_cd.new(level=level, main=main, category=category, subcategory=subcategory,
                           main_add=main_add, category_add=category_add, name=name)



async def main_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=2)

    maines = await get_main()

    for main in maines:
        #number_of_items = await count_items(main.main_code)
        button_text = f"{main.main_name}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           main=main.main_code)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup

async def categories_keyboard(main):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=2)

    categories = await get_categories(main)
    for category in categories:
        # number_of_items = await count_items(main_code=main,
        #                                     category_code=category.category_code)
        button_text = f"{category.category_name}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           main=main,
                                           category=category.category_code)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1, main=main)
        )
    )
    return markup

async def subcategories_keyboard(main, category):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=2)

    subcategories = await get_subcategories(category)
    for subcategory in subcategories:
        # number_of_items = await count_items(main_code=main, category_code=category,
        #                                     subcategory_code=subcategory.subcategory_code)
        button_text = f"{subcategory.subcategory_name}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           main=main,
                                           category=category,
                                           subcategory=subcategory.subcategory_code)
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1, main=main)
        )
    )
    return markup

async def make_order_keyboard(main, category, subcategory):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup(row_width=2)

    item = await get_item(main_code=main, category_code=category, subcategory_code=subcategory)
    adds_select = item[0].adds
    adds = await get_categories_add()
    for add in adds:
        if add.category_name.lower() in adds_select:

            button_text = f"{add.category_name}"
            callback_data = make_callback_data(level=CURRENT_LEVEL + 1, main=main,
                                               category=category, subcategory=subcategory,
                                               category_add=add.category_code)
            markup.insert(
                InlineKeyboardButton(text=button_text, callback_data=callback_data)
            )
    markup.row(
        InlineKeyboardButton(
            text="ДОБАВИТЬ ЗАКАЗ В КОРЗИНУ",
            callback_data=basket_add_cd.new(add=True)
        )
    )

    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1, main=main, category=category,
                                             subcategory=subcategory)
                                 )
               )

    return markup

async def adds_keyboard(main, category, subcategory, category_add):
    CURRENT_LEVEL = 4
    markup = InlineKeyboardMarkup(row_width=2)
    item = await get_item(main_code=main, category_code=category, subcategory_code=subcategory)
    volume = item[0].volume
    adds = await get_adds(category_add)
    for add in adds:
        if category_add == "1_v":          # проверка на наличие объема
            if add.name in volume:
                button_text = f"{add.name}"
                callback_data = make_callback_data(level=CURRENT_LEVEL - 1, main=main,
                                                   category=category, subcategory=subcategory,
                                                   category_add=category_add, name=add.category_code[0] + add.name)
                markup.insert(
                    InlineKeyboardButton(text=button_text, callback_data=callback_data)
                )
        else:
            button_text = f"{add.name}"
            callback_data = make_callback_data(level=CURRENT_LEVEL - 1, main=main,
                                               category=category, subcategory=subcategory,
                                               category_add=category_add, name=add.category_code[0] + add.name)
            markup.insert(
                InlineKeyboardButton(text=button_text, callback_data=callback_data)
            )

    if category_add != "1_v":
        markup.row(
            InlineKeyboardButton(
                text="Оставить как есть",
                callback_data=make_callback_data(level=CURRENT_LEVEL - 1, main=main, category=category,
                                                 subcategory=subcategory)
            )
        )


    return markup


# async def item_keyboard(main, category, subcategory):
#     CURRENT_LEVEL = 3
#
#     markup = InlineKeyboardMarkup(row_width=1)
#
#     item = await get_item(main, category, subcategory)
#     for item in items:
#         button_text = f"{item.name} - ₽{item.price}"
#         callback_data = make_callback_data(level=CURRENT_LEVEL + 1, main=main,
#                                            category=category, subcategory=subcategory,
#                                            item_id=item.id)
#         markup.insert(
#             InlineKeyboardButton(text=button_text, callback_data=callback_data)
#         )
#
#
#     markup.row(
#         InlineKeyboardButton(
#             text="Назад",
#             callback_data=make_callback_data(level=CURRENT_LEVEL - 1, main=main, category=category)
#         )
#     )
#     return markup

# async def item_keyboard(main, category, subcategory, item_id, count_item):
#     CURRENT_LEVEL = 4
#     markup = InlineKeyboardMarkup()
#     # item = await get_item(item_id)
#     markup.row(
#         InlineKeyboardButton(text=f"Добавить в корзину - {count_item}",
#                              callback_data=buy_item.new(item_id=item_id))
#     )
#
#     CURRENT_LEVEL_ADD = 0
#
#     maines_add = await get_main_add()
#     for main_add in maines_add:
#
#         button_text = f"Добавить сироп, молоко, мед и др."
#         callback_data = make_callback_data_add(main=main,
#                                                category=category, subcategory=subcategory,
#                                                item_id=item_id,
#                                                level_add=CURRENT_LEVEL_ADD + 1,
#                                                main_add=main_add.main_code)
#         markup.row(
#             InlineKeyboardButton(text=button_text, callback_data=callback_data)
#         )
#
#     markup.row(
#         InlineKeyboardButton(
#             text="Назад",
#             callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
#                                              main=main,
#                                              category=category,
#                                              subcategory=subcategory,
#                                              item_id=item_id
#                                              )
#         )
#     )
#     return markup
#
# async def category_add_keyboard(main, category, subcategory, item_id,
#                                 main_add):
#     CURRENT_LEVEL_ADD = 1
#     markup = InlineKeyboardMarkup(row_width=2)
#     categories_add = await get_categories_add(main_add)
#     for category_add in categories_add:
#
#         button_text = f"{category_add.category_name}"
#         callback_data = make_callback_data_add(main=main,
#                                                category=category, subcategory=subcategory,
#                                                item_id=item_id,
#                                                level_add=CURRENT_LEVEL_ADD + 1,
#                                                main_add=main_add,
#                                                category_add=category_add.category_code)
#         markup.insert(
#             InlineKeyboardButton(text=button_text, callback_data=callback_data)
#         )
#
#     markup.row(
#         InlineKeyboardButton(
#             text="Назад",
#             callback_data=make_callback_data(level=4,
#                                              main=main,
#                                              category=category,
#                                              subcategory=subcategory,
#                                              item_id=item_id
#                                              )
#         )
#     )
#     return markup
#
# async def adds_keyboard(main, category, subcategory, item_id, main_add, category_add):
#     CURRENT_LEVEL_ADD = 2
#     markup = InlineKeyboardMarkup(row_width=2)
#
#     adds = await get_adds(main_add, category_add)
#     for add in adds:
#
#         button_text = f"{add.name}"
#         callback_data = make_callback_data_add(main=main,
#                                                category=category,
#                                                subcategory=subcategory,
#                                                item_id=item_id,
#                                                level_add=CURRENT_LEVEL_ADD + 1,
#                                                main_add=main_add,
#                                                category_add=category_add,
#                                                add_id=add.id)
#         markup.insert(
#             InlineKeyboardButton(text=button_text, callback_data=callback_data)
#         )
#
#     markup.row(
#         InlineKeyboardButton(
#             text="Назад",
#             callback_data=make_callback_data_add(main=main,
#                                                  category=category,
#                                                  subcategory=subcategory,
#                                                  item_id=item_id,
#                                                  level_add=CURRENT_LEVEL_ADD - 1,
#                                                  main_add=main_add,
#                                                  category_add=category_add)
#         )
#     )
#     return markup
#
# async def add_keyboard(main, category, subcategory, item_id,
#                        main_add, category_add, add_id, count_add):
#     CURRENT_LEVEL_ADD = 3
#     markup = InlineKeyboardMarkup()
#     markup.row(
#         InlineKeyboardButton(text=f"Добавить - {count_add}", callback_data=buy_add.new(add_id=add_id))
#     )
#
#     markup.row(
#         InlineKeyboardButton(
#             text="Назад",
#             callback_data=make_callback_data_add(level_add=CURRENT_LEVEL_ADD - 1,
#                                              main=main,
#                                              category=category,
#                                              subcategory=subcategory,
#                                              item_id=item_id,
#                                              main_add=main_add,
#                                              category_add=category_add
#                                              )
#         )
#     )
#     return markup








