import psycopg2
from psycopg2 import Error



def db_connect():
    global connection, cursor
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="141019911",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="testdb")
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(connection.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute('''CREATE TABLE IF NOT EXISTS menu
                            (img TEXT, 
                            name TEXT PRIMARY KEY,
                            description TEXT,
                            price TEXT)''')
        connection.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    # finally:
    #     if connection:
    #         cursor.close()
    #         connection.close()
    #         print("Соединение с PostgreSQL закрыто")


async def sql_add_command(state):
    async with state.proxy() as data:
        try:
            cursor.execute('INSERT INTO menu VALUES (%s, %s, %s, %s)', tuple(data.values()))
            connection.commit()
            print('Успешно загрузили данные')
        except (Exception, Error) as error:
            print("Ошибка при загрузке данных с PostgreSQL", error)

async def sql_get_menu(message,bot):
    cursor.execute('SELECT * FROM menu')
    menu = cursor.fetchall()
    for list in menu:
            await bot.send_photo(message.from_user.id, list[0], f'{list[1]}\nОписание: {list[2]}\nЦена: {list[-1]}')

async def sql_delete_command(data):
    cursor.execute('DELETE FROM menu WHERE name = %s', (data,))

async def sql_read2():
    cursor.execute('SELECT * FROM menu')
    return cursor.fetchall()
