print()     # Отступ

# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)

# Описание функции:
# add_everything_up(a, b) принимает a и b,
# которые могут быть как числами(int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой),
# то возвращать строковое представление этих двух данных вместе (в том же порядке).
# Во всех остальных случаях выполнять стандартные действия.


def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b

        elif isinstance(a, str) and isinstance(b, str):
            result = a + b

        elif isinstance(a, str) and isinstance(b, (int, float)):
            result = a + str(b)

        elif isinstance(a, (int, float)) and isinstance(b, str):
            result = str(a) + b

    except TypeError as e:
        print(e)
        result = str(a) + str(b)

    return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
# print(add_everything_up(True, 7))
# print(add_everything_up(True, 'строка'))
# print(add_everything_up('str - ', 'строка'))
