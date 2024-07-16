import io
from pprint import pprint


print()      # Отступ


# Создайте функцию custom_write(file_name, strings), которая принимает аргументы
# file_name - название файла для записи,
# strings - список строк для записи.
def custom_write(file_name, strings):
    # Функция должна:
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    line_number = 1

    # Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    for string in strings:
        # Для получения номера байта начала строки используйте метод tell() перед записью.
        position = file.tell()
        file.write(string + '\n')

        # (<номер строки>, <байт начала строки>), а значением - записываемая строка.
        strings_positions[(line_number, position)] = string
        line_number += 1
    file.close()

    # Возвращать словарь strings_positions, где ключом будет кортеж
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

