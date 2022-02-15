from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram import types, Dispatcher
from keyboards import kb_client
from dispatcher_bot.dispatcher import bot, dp
from states import bot_db
from keyboards.inline import urlkb, inkb
from aiogram.dispatcher.filters import Text

# @dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    try:
        # await message.answer( 'Привет! Проверь личные сообщения ;)')
        await bot.send_message(message.from_user.id, 'Привет!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через личные сообщения. Напишите ему: \n@Farming_hot_bot')

# @dp.message_handler(commands=['Режим_работы'])    
async def working_time(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт c 8:00 до 22:00, Сб-Вс с 9:00 до 20:00')


# @dp.message_handler(commands=['Расположение'])    
async def working_geo(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул.Ленина Дом Короля')

# @dp.message_handler(commands=['Меню'])    
async def menu_list(message: types.Message):
    await bot_db.sql_get_menu(message, bot)

# @dp.message_handler(commands='Ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки: ', reply_markup=urlkb)

# @dp.message_handler(commands='test')
# async def test_command(message: types.Message):
#     await message.answer('test: ', reply_markup=inkb)

# answ = dict()

# @dp.callback_query_handler(Text(startswith='like_'))
# async def test_Callback(callback: types.CallbackQuery):
#     res = int(callback.data.split('_')[1])
#     if f'{callback.from_user.id}' not in answ:
#         answ[f'{callback.from_user.id}'] = res
#         await callback.answer('Вы проголосовали')
#     else:
#         await callback.answer('Вы уже проголосовали', show_alert=True)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(working_time, commands=['Режим_работы'])
    dp.register_message_handler(working_geo, commands=['Расположение'])
    dp.register_message_handler(menu_list, commands=['Меню'])
    dp.register_message_handler(url_command, commands=['Ссылки'])
    # dp.register_message_handler(test_command, commands=['test'])
