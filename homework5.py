print() # Отступ

# Задайте переменные разных типов данных:
# - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = tuple([1, 2, 3, True, 'String'])

# - Выполните операции вывода кортежа immutable_var на экран.
print('Immutable tuple:', immutable_var)

# Изменение значений переменных:
# - Попытайтесь изменить элементы кортежа immutable_var.
# immutable_var[0] = 200
# Объясните, почему нельзя изменить значения элементов кортежа.
# Ответ: кортеж не поддерживает обращение по элементам.

# Создание изменяемых структур данных:
# - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = [1, 2, 3, True, 'String']

# - Измените элементы списка mutable_list.
mutable_list[0] = 'Modified'

# - Выведите на экран измененный список mutable_list.
print(mutable_list)
