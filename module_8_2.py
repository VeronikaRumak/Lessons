print()     # Отступ


# Напишите 2 функции:

# Функция personal_sum(numbers):
# Должна принимать коллекцию numbers.
def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    # Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
    for i in numbers:
        try:
            result += i

        # Если же при переборе встречается данное типа отличного от числового,
        # то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
        except TypeError:
            print(f'Некорректный тип данных для подсчета суммы - {i}')
            incorrect_data += 1

    # В конечном итоге функция возвращает кортеж из двух значений:
    # result - сумма чисел, incorrect_data - кол-во некорректных данных.
    return result, incorrect_data


# Функция calculate_average(numbers)
def calculate_average(numbers):
    try:
        # Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
        # Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
        total_sum, incorrect_data = personal_sum(numbers)

        # Среднее арифметическое - сумма всех данных делённая на их количество.
        return total_sum / (len(numbers) - incorrect_data)

    # Т.к. коллекция numbers может оказаться пустой,
    # то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
    except ZeroDivisionError:
        return 0

    # Также в numbers может быть записана не коллекция, а другие типы данных,
    # например числа. Обработайте исключение TypeError выводя строку
    # 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None.
    except TypeError:
        print('В numbers записан некорректный тип данных')


# Строка перебирается, но каждый символ - строковый тип
print(f'Результат 1: {calculate_average("1, 2, 3")}')

# Учитываются только 1 и 3
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')

# Передана не коллекция
print(f'Результат 3: {calculate_average(567)}')

# Всё должно работать
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
