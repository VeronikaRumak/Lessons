import sqlite3

print()     # Отступ

# Создайте файл базы данных not_telegram.db и подключитесь к ней,
# используя встроенную библиотеку sqlite3.
connection = sqlite3.connect('not_telegram.db')

# Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
cursor = connection.cursor()

# Создайте таблицу Users, если она ещё не создана.
# В этой таблице должны присутствовать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число
# balance - целое число (не пустой)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Заполните её 10 записями:
# User1, example1@gmail.com, 10, 1000
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 1000
# ...
# User10, example10@gmail.com, 100, 1000
users_data = []
for i in range(1, 11):
    users_data.append((i, f'User{i}', f'example{i}@gmail.com', i * 10, 1000))
cursor.executemany('INSERT INTO Users ' '(id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)', users_data)

# Фиксация изменений
connection.commit()

# Обновление balance у каждой 2ой записи начиная с 1ой на 500
cursor.execute('''
UPDATE Users
SET balance = balance - 500
WHERE id % 2 = 1
''')

# Фиксация изменений
connection.commit()

# Удалите из базы данных not_telegram.db запись с id = 6.
cursor.execute('''
DELETE FROM Users
WHERE id = 6
''')

# Фиксация изменений
connection.commit()

# Подсчитать общее количество записей.
cursor.execute('''
SELECT COUNT(*) FROM Users
''')
total_users = cursor.fetchone()[0]

# Посчитать сумму всех балансов.
cursor.execute('''
SELECT SUM(balance) FROM Users
''')
all_balances = cursor.fetchone()[0]

# Вывести в консоль средний баланс всех пользователя.
if total_users > 0:
    average_balance = all_balances / total_users
    print(f'Средний баланс всех пользователей: {average_balance}')

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и
cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

# выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
rows = cursor.fetchall()
for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

# Закрытие соединения с базой данных
connection.close()
