from math import inf

print()  # Отступ


# В true_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать бесконечность.
# Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)


def divide(first, second):
    result = 0
    if second == 0:
        return inf
    else:
        result = first / second
    return result
