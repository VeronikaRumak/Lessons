import sqlite3


print()     # Отступ


connection = sqlite3.connect('initiate_db.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
)
''')

# initiate_db дополните созданием таблицы Users, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число (не пустой)
# balance - целое число (не пустой)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
)
''')


# Дополните файл crud_functions.py, написав и дополнив в нём следующие функции:
def get_all_products():
    products_data = []
    for i in range(1, 5):
        products_data.append((i, f'Мяч {i}', f'Описание {i}', i * 100))

    cursor.executemany('INSERT INTO Products (id, title, description, price) '
                       'VALUES (?, ?, ?, ?)', products_data)

    connection.commit()

    cursor.execute('''
        SELECT title, description, price
        FROM Products
        ''')

    products = cursor.fetchall()
    connection.close()

    return products


# add_user(username, email, age), которая принимает: имя пользователя, почту и возраст.
# Данная функция должна добавлять в таблицу Users вашей БД запись с переданными данными.
# Для добавления записей в таблице используйте SQL запрос.
def add_user(username, email, age):
    # Баланс у новых пользователей всегда равен 1000.
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    if cursor.fetchone() is None:
        cursor.execute('''
            INSERT INTO Users (username, email, age, balance)
            VALUES (?, ?, ?, 1000)
        ''', (username, email, age))
        connection.commit()


# is_included(username) принимает имя пользователя и возвращает True,
# если такой пользователь есть в таблице Users, в противном случае False.
# Для получения записей используйте SQL запрос.
def is_included(username):
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    return cursor.fetchone() is not None




