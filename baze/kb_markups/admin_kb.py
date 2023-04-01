from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#Кнопки админа

button_load = KeyboardButton('/Завантажити')
button_delete = KeyboardButton('/Видалити')
button_back = KeyboardButton('/Вихід')
button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
             .add(button_delete).add(button_back)