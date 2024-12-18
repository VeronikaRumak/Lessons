print()


# Задача 1 (просто) "Арифметика":
# Напишите в начале программы однострочный комментарий: "1st program".
# Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5,
# после умножение на 5.
# Предполагаемый результат: 15.0
print(9 ** 0.5 * 5)


# Задача 2 (просто) "Логика":
# Напишите в начале программы однострочный комментарий: "2nd program".
# Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно,
# выведете результат на экран(в консоль)
# Предполагаемый результат: True
print(9.99 > 9.98 and 1000 != 1000.1)


# Задача 3 (средне) "Школьная загадка":
# Напишите в начале программы однострочный комментарий: "3rd program".
# Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 без приоритета.
print(2 * 2 + 2)
# Выведите на экран(в консоль) 2 умноженное на 2 плюс 2 с приоритетом для сложения.
print(2 * (2 + 2))
# Выведите на экран(в консоль) результат сравнения этих двух выражений.
print(2 * 2 + 2 == 2 * (2 + 2))
# Предполагаемый результат (с использованием ==): False


# Задача 4 (сложно) "Первый после точки":
# Напишите в начале программы однострочный комментарий: "4th program".
# Начало алгоритма решения:

# Следующие шаги алгоритма составьте самостоятельно.
# В них вам понадобится команда int() и остаточное деление на 10.

# Дана строка '123.456'.
number_str = '123.456'

# Преобразуйте в строку в дробное число. ('123.456' -> 123.456)
number_float = float(number_str)

# Умножьте на 10, чтобы сместить 4 в целую часть. (1234.56)

number_shifted = number_float * 10

# Вывести на экран первую цифру после запятой - 4.
number_int = int(number_shifted)
first_digit_after_dot = number_int % 10


print(first_digit_after_dot)