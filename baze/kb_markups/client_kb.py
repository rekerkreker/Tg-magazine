from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton('/Час-роботи')
button2 = KeyboardButton('/Оплата')
button3 = KeyboardButton('/Меню')
button4 = KeyboardButton('/Купити')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
#one_time_keyboard=True одноразовая клавиатру
# kb_client.add(button1).add(button2).insert(button3) 

kb_client.row(button1, button2 , button3, button4)