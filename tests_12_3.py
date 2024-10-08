import runner_and_tournament as r_and_t
import unittest


print()     # Отступ


# Напишите класс TournamentTest, наследованный от TestCase.
class TournamentTest(unittest.TestCase):
    # TournamentTest атрибутом is_frozen = True.
    is_frozen = True

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
    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
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


class RunnerTest(unittest.TestCase):
    # Классы RunnerTest дополнить атрибутом is_frozen = False
    is_frozen = False

    # В классе пропишите следующие методы:

    # test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
    @unittest.skipIf(False, '')
    def test_walk(self):
        runner = r_and_t.Runner("Runner1")

        # Далее вызовите метод walk у этого объекта 10 раз.
        for _ in range(10):
            runner.walk()

        # После чего методом assertEqual сравните distance этого объекта со значением 50.
        self.assertEqual(runner.distance, 50)

    # test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
    @unittest.skipIf(False, '')
    def test_run(self):
        runner = r_and_t.Runner("Runner2")

        # Далее вызовите метод run у этого объекта 10 раз.
        for _ in range(10):
            runner.run()

        # После чего методом assertEqual сравните distance этого объекта со значением 100.
        self.assertEqual(runner.distance, 100)

    # test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
    @unittest.skipIf(False, '')
    def test_challenge(self):
        runner1 = r_and_t.Runner("Runner3")
        runner2 = r_and_t.Runner("Runner4")

        # Далее 10 раз у объектов вызываются методы run и walk соответственно.
        for _ in range(10):
            runner1.run()
            runner2.walk()

        # Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
        # чтобы убедится в неравенстве результатов.
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()


