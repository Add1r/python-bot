from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


urlkb = InlineKeyboardMarkup(row_width=1)

urlButton = InlineKeyboardButton(text='Ссылка', url='https://google.com')
urlButton2 = InlineKeyboardButton(text='Ссылка', url='https://t-do.ru/Test_of_football_bot')
x = [InlineKeyboardButton(text='Ссылка', url='https://google.com'), InlineKeyboardButton(text='Ссылка', url='https://google.com'), InlineKeyboardButton(text='Ссылка', url='https://google.com')]

urlkb.add(urlButton, urlButton2).row(*x)

inkb = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='like', callback_data='like_1'),\
                                            InlineKeyboardButton(text='dislike', callback_data='like_-1'))