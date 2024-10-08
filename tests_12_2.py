import runner_and_tournament as r_and_t
import unittest


print()     # Отступ


# Напишите класс TournamentTest, наследованный от TestCase.
class TournamentTest(unittest.TestCase):

    # В нём реализуйте следующие методы:

    # setUpClass - метод, где создаётся атрибут класса all_results.
    @classmethod
    def setUpClass(cls):

        # Это словарь в который будут сохраняться результаты всех тестов.
        cls.all_results = {}

    # setUp - метод, где создаются 3 объекта:
    def setUp(self):
        # Бегун по имени Усэйн, со скоростью 10.
        self.usein = r_and_t.Runner("Усэйн", 10)

        # Бегун по имени Андрей, со скоростью 9.
        self.andrey = r_and_t.Runner("Андрей", 9)

        # Бегун по имени Ник, со скоростью 3.
        self.nick = r_and_t.Runner("Ник", 3)

    # tearDownClass - метод, где выводятся all_results по очереди в столбец.
    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    # Напишите 3 таких метода, где в забегах участвуют
    # (порядок передачи в объект Tournament соблюсти):
    # Усэйн и Ник
    # Андрей и Ник
    # Усэйн, Андрей и Ник.
    # Как можно понять: Ник всегда должен быть последним.

    # Так же методы тестирования забегов,
    # в которых создаётся объект Tournament на дистанцию 90.
    def test_race_usein_nick(self):

        # У объекта класса Tournament запускается метод start,
        tournament = r_and_t.Tournament(93, self.usein, self.nick)

        result = tournament.start()

        # который возвращает словарь в переменную all_results.
        self.all_results[len(self.all_results) + 1] = result

        # В конце вызывается метод assertTrue,
        # в котором сравниваются последний объект из all_results (брать по наибольшему ключу)
        # и предполагаемое имя последнего бегуна.
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_andrey_nick(self):

        # У объекта класса Tournament запускается метод start,
        tournament = r_and_t.Tournament(90, self.andrey, self.nick)

        result = tournament.start()

        # который возвращает словарь в переменную all_results.
        self.all_results[len(self.all_results) + 1] = result

        # В конце вызывается метод assertTrue,
        # в котором сравниваются последний объект из all_results (брать по наибольшему ключу)
        # и предполагаемое имя последнего бегуна.
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_usein_andrey_nick(self):

        # У объекта класса Tournament запускается метод start,
        tournament = r_and_t.Tournament(90, self.usein, self.andrey, self.nick)

        result = tournament.start()

        # который возвращает словарь в переменную all_results.
        self.all_results[len(self.all_results) + 1] = result

        # В конце вызывается метод assertTrue,
        # в котором сравниваются последний объект из all_results (брать по наибольшему ключу)
        # и предполагаемое имя последнего бегуна.
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()


