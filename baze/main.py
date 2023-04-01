from aiogram import Bot, Dispatcher , executor, types
from data_base import sqlite_db
import logging
import os, json, string
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

token = '5842915630:AAF9RuxKdVbWmGHP1dL9Bgy5kLlQnXT3Fqs'

logging.basicConfig(level=logging.INFO)
bot = Bot(token = token)
dp = Dispatcher(bot, storage=MemoryStorage())

async def on_startup(_):
    print('BOT ONLINE')
    sqlite_db.sql_start()


from handlers import client, admin, other

client.register_handler_client(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)