import sqlite3


print()     # Отступ


# Создайте файл crud_functions.py и напишите там следующие функции:

# get_all_products, которая возвращает все записи из таблицы Products,
# полученные при помощи SQL запроса.
def get_all_products():
    # initiate_db, которая создаёт таблицу Products,
    # если она ещё не создана при помощи SQL запроса.
    connection = sqlite3.connect('initiate_db.db')

    # Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
    cursor = connection.cursor()

    # Эта таблица должна содержать следующие поля:
    # id - целое число, первичный ключ
    # title(название продукта) - текст (не пустой)
    # description(описание) - текст
    # price(цена) - целое число (не пустой)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')

    products_data = []
    for i in range(1, 5):
        products_data.append((i, f'Мяч {i}', f'Описание {i}', i * 100))

    cursor.executemany('INSERT INTO Products (id, title, description, price) '
                       'VALUES (?, ?, ?, ?)', products_data)

    # Фиксация изменений
    connection.commit()

    cursor.execute('''
        SELECT title, description, price
        FROM Products
        ''')
    products = cursor.fetchall()
    connection.close()
    return products






