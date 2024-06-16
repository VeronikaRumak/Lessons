print()  # Отступ


# В fake_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать строку 'Ошибка'.

def divide(first, second):
    result = 0
    if second == 0:
        return 'Ошибка'
    else:
        result = first / second
    return result
