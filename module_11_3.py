# Интроспекция - это способность объекта во время выполнения программы получить тип,
# доступные атрибуты и методы, а также другую информацию,
# которая необходима нам для выполнения дополнительных операций с объектом.

import requests
import inspect
import pprint

print()     # Отступ


# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и
# проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
def introspection_info(obj):

    # Словарь для 3-го пункта
    info = {}

    # 2. Используйте встроенные функции и методы интроспекции Python для получения информации
    # о переданном объекте.
    # 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:

    #   - Тип объекта.
    info['type'] = type(obj).__name__

    #   - Атрибуты объекта.
    attributes = [attribute

                  # Используется dir(obj) для получения списка всех атрибутов и методов объекта.
                  for attribute in dir(obj)

                  # Фильтруются только атрибуты,
                  # которые не являются вызываемыми (CALLABLE)
                  # GETATTR используется для получения значения атрибута объекта по его имени

                  # и не начинаются с '__' (STARTSWITH) - принимает один или несколько аргументов,
                  # которые представляют собой подстроки, с которыми сравнивается начало строки.
                  if not callable(getattr(obj, attribute)) and not attribute.startswith('__')]

    info['attributes'] = attributes

    #   - Методы объекта.
    methods = [method
               for method in dir(obj)
               if callable(getattr(obj, method)) and not method.startswith('__')]
    info['methods'] = methods

    #   - Модуль, к которому объект принадлежит.

    # Функция GETATTR используется для получения значения атрибута объекта.
    # Первый аргумент OBJ — это объект, из которого мы хотим получить атрибут.

    # Второй аргумент '__module__' — это имя атрибута, который мы хотим получить.
    # Атрибут __module__ содержит имя модуля, в котором определен объект.

    # Третий аргумент 'N/A' — это значение по умолчанию, которое будет возвращено,
    # если атрибут __module__ не существует.
    info['module'] = getattr(obj, '__module__', 'N/A')

    return info


number_info = introspection_info(42)
print(number_info)


class ExampleClass:
    def __init__(self, value):
        self.value = value

    def example_method(self):
        pass


example_instance = ExampleClass(10)
class_info = introspection_info(example_instance)
print(class_info)





