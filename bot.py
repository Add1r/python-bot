from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.utils import executor
from dispatcher_bot.dispatcher import dp
from handlers import client, admin
from states import bot_db


async def on_start(dispatcher: Dispatcher):
    print('Бот погнал работать!')
    bot_db.db_connect()


async def on_shutdown(dispatcher: Dispatcher):
    dp.storage.close()
    dp.storage.wait_closed()
    print('Бот ушёл отдыхать!')

    
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start, on_shutdown=on_shutdown)