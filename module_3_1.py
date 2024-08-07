print()     # Отступ


# Вам необходимо написать 3 функции:

# Создать переменную calls = 0 вне функций.
calls = 0


# Функция count_calls подсчитывающая вызовы остальных функций.
# Создать функцию count_calls и изменять в ней значение переменной calls.
# Эта функция должна вызываться в остальных двух функциях.
def count_calls():
    global calls
    calls += 1


# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки,
# строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case


# Создать функцию is_contains с двумя параметрами string и list_to_search,
# реализовать логику работы по описанию.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True,
# если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(string, list_to_search):
    count_calls()
    lower_string = string.lower()
    lower_list = []
    for i in list_to_search:
        lower_list.append(i.lower())
    return lower_string in lower_list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

