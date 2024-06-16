print()  # Отступ


# А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?

# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)

# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов,
# можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.

# Создаем функцию calculate_structure_sum и прописываем параметр *args,
# в который будет входить неограниченное количество переменных
def calculate_structure_sum(*args):
    summ = 0
    # Цикл для перебирания содержимого в параметре
    for i in args:
        # isinstance - проверяет к какому типу данных относится входящая переменная
        if isinstance(i, int):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, dict):
            # Используем рекурсию для словаря, так как в нем есть ключи и значение,
            # которые могут относиться к разным типам данных
            summ += calculate_structure_sum(*i.items())
        # list, tuple, set - похожие типы данных, поэтому внесены в один elif
        elif isinstance(i, (list, tuple, set)):
            # Используем рекурсию для этих типов данных, так как в них могут храниться разные
            # типы данных
            summ += calculate_structure_sum(*i)
    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
