from aiogram import Bot, Dispatcher , executor, types
import logging
import os, json, string

from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = '5842915630:AAF9RuxKdVbWmGHP1dL9Bgy5kLlQnXT3Fqs'

storage=MemoryStorage

logging.basicConfig(level=logging.INFO)
bot = Bot(token = token)
dp = Dispatcher(bot, storage=MemoryStorage())

