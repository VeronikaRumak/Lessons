import rt_with_exceptions as rt
import logging as log
import unittest


print()     # Отступ


# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig
# на следующие параметры:
log.basicConfig(
                # Уровень - INFO
                level=log.INFO,
                # Режим - запись с заменой('w')
                filemode='w',
                # Название файла - runner_tests.log
                filename='runner_tests.log',
                # Кодировка - UTF-8
                encoding='UTF-8',
                # Формат вывода - на своё усмотрение, обязательная информация:
                # уровень логирования, сообщение логирования.
                format='%(asctime)s | %(levelname)s | %(message)s')


# Дополните методы тестирования в классе RunnerTest следующим образом:
class RunnerTest(unittest.TestCase):
    
    # test_walk:
    def test_walk(self):
        # Оберните основной код иконструкцией try-except.
        try:
            # При создани объекта Runner передавайте отрицательное значение в speed.
            runner = rt.Runner("Runner1", speed=-12)
            runner.walk()

            # В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
            log.info('"test_walk" выполнен успешно')

        # В блоке except обработайте исключение соответствующего типа и
        except ValueError as err:

            # логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
            log.warning("Неверная скорость для Runner")

    # test_run:
    def test_run(self):

        # Оберните основной код конструкцией try-except.
        try:
            # При создании объекта Runner передавайте что-то кроме строки в name.
            runner = rt.Runner(1, 12)
            runner.run()

            # В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
            log.info('"test_run" выполнен успешно')

        # В блоке except обработайте исключение соответствующего типа и
        # логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
        except TypeError as err:
            log.warning("Неверный тип данных для объекта Runner")


if __name__ == '__main__':
    unittest.main()







