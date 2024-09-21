
import tests_12_3
import unittest
import inspect

print()     # Отступ


# Часть 1. TestSuit.

# Укажите на него переменной с произвольным названием.
test_suit = unittest.TestSuite()

# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
test_suit.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_suit.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

# Создайте объект класса TextTestRunner, с аргументом verbosity=2.
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suit)


# Часть 2. Пропуск тестов.

# Классы RunnerTest дополнить атрибутом is_frozen = False и
# TournamentTest атрибутом is_frozen = True.

# Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении
# is_frozen = False будет выполнять тесты,
# а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.





