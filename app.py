from aiogram import executor

import middlewares, filters, handlers
from utils.db_api import database
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import dp, db


async def on_startup(dispatcher):
    print("Подключаем БД")
    await database.create_db()


    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    #await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

