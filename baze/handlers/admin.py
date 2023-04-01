from aiogram import types, Dispatcher
from create_bot import dp, bot 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os, json, string
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from kb_markups import admin_kb
from kb_markups import kb_client
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    # admin = State()

#вход с помощью админки
# @dp.message_handler(commands=['admin'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Ви війшли в адмінку', reply_markup=admin_kb.button_case_admin)
    await message.delete()
    

async def command_back(message:types.Message, state:FSMContext):
    await state.finish()
    await message.reply('Ви вийшли з адмін панелі', reply_markup = kb_client)

#Загрузка фото 
# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Завантажте фото: ')


#выход в любой момент через слово отмена
async def cancel_handler(message: types.Message, state:FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK', reply_markup = kb_client)



# @dp.message_handler(content_types=['photo'], state=FsmAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id 
        await FSMAdmin.next()
        await message.reply("Назва: ")



# @dp.message_handler(state=FsmAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("Введіть опис: ")



# @dp.message_handler(state=FsmAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply("Ціна: ")


# @dp.message_handler(state=FsmAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price']= float(message.text)
 
    
    await sqlite_db.sql_add_command(state)
    await state.finish()
    await message.reply("Ви додали товар: ")

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del'))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del',''))
    await callback_query.answer(text=f'{callback_query.data.replace("del", "")} видалена.', show_alert=True)
    print('delete1')


    
# @dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n Опис: {ret[2]}\nЦіна {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                add(InlineKeyboardButton(f'Видалити {ret[1]}', callback_data=f'del{ret[1]}')))
    print('delete2')


def register_handler_admin(dp : Dispatcher):
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del'))
    dp.register_message_handler(delete_item, commands='Видалити')
    dp.register_message_handler(command_back, state="*", commands='Вихід')
    dp.register_message_handler(cm_start, commands=['Завантажити'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='Відміна')
    dp.register_message_handler(cancel_handler, Text(equals='Відміна', ignore_case=True), state="*")
    dp.register_message_handler(make_changes_command, commands=['admin'], is_chat_admin=True)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['admin'], is_chat_admin=True)