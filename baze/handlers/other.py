from aiogram import types, Dispatcher
import json, string 
from create_bot import dp, bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage


@dp.message_handler()
async def no_mat(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('mute.json')))) != set():
        await message.reply('Мати заборонені')
        await message.delete()


def register_handler_other(dp:Dispatcher):
     dp.register_message_handler(no_mat)
