from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/Меню')
b3 = KeyboardButton('/Режим_работы')
b4 = KeyboardButton('/Расположение')
b5 = KeyboardButton('Поделится номером', request_contact=True)
b6 = KeyboardButton('Поделится геопозицией', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6)
# kb_client.add(b1).add(b2) кнопки с новой строки
# kb_client.row(b1,b2) все в строку