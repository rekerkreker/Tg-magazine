from aiogram import types, Dispatcher
from create_bot import dp, bot 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from kb_markups import kb_client
from data_base import sqlite_db


@dp.message_handler(commands=['start', 'help'])
async def commands_start(message:types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привіт хочеш собі крутий шолом?', reply_markup = kb_client)
        await message.delete
    except:
        await message.reply('Напиши мені у особисті повідомленя:\nhttps://t.me/UkrainianHelmet_bot')


@dp.message_handler(commands=['Час-роботи'])
async def commands_time(message:types.Message):
    await message.answer('⏱Працюємо з Пн-Пт з 9 до 20:00 , Сб-Вс з 10 до 22:00')

@dp.message_handler(commands=['Купити'])
async def commands_buy(message:types.Message):
    await message.answer('Напиши йому: https://t.me/Chifya_Aboba за замовленням')


@dp.message_handler(commands=['Оплата'])
async def commands_pay(message:types.Message):
    await bot.send_message(message.from_user.id, 
    "Спосіб оплати на карту \n 0000 0000 0000 0000 visa")
    print("test5")
    
@dp.message_handler(commands=['Меню'])
async def helmet_menu_command(message:types.Message):
    await sqlite_db.sql_read(message)
    print("test4")
def register_handler_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(commands_time, commands=['Час-роботи'])
    dp.register_message_handler(commands_pay, commands=['Оплата'])
    dp.register_message_handler(helmet_menu_command, commands=['Меню'])
    dp.register_message_handler(commands_start, commands=['help'])
    dp.register_message_handler(commands_buy, commands=['Купити'])