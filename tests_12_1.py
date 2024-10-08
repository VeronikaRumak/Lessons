import runner as r
import unittest


print()     # Отступ


# В этом коде сможете обнаружить класс Runner,
# объекты которого вам будет необходимо протестировать.

# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest.
class RunnerTest(unittest.TestCase):
    # В классе пропишите следующие методы:

    # test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
    def test_walk(self):
        runner = r.Runner("Runner1")

        # Далее вызовите метод walk у этого объекта 10 раз.
        for _ in range(10):
            runner.walk()

        # После чего методом assertEqual сравните distance этого объекта со значением 50.
        self.assertEqual(runner.distance, 50)

    # test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
    def test_run(self):
        runner = r.Runner("Runner2")

        # Далее вызовите метод run у этого объекта 10 раз.
        for _ in range(10):
            runner.run()

        # После чего методом assertEqual сравните distance этого объекта со значением 100.
        self.assertEqual(runner.distance, 100)

    # test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
    def test_challenge(self):
        runner1 = r.Runner("Runner3")
        runner2 = r.Runner("Runner4")

        # Далее 10 раз у объектов вызываются методы run и walk соответственно.
        for _ in range(10):
            runner1.run()
            runner2.walk()

        # Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
        # чтобы убедится в неравенстве результатов.
        self.assertNotEqual(runner1.distance, runner2.distance)


# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
if __name__ == '__main__':
    unittest.main()





