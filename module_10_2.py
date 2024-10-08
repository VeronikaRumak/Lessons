from threading import Thread
import time

print()     # Отступ


# Создайте класс Knight,
# наследованный от Thread, объекты которого будут обладать следующими свойствами:
class Knight(Thread):
    res = []

    def __init__(self, name, power):
        super().__init__()

        # Атрибут name - имя рыцаря. (str)
        self.name = name

        # Атрибут power - сила рыцаря. (int)
        self.power = power

        self.enemies = 100
        self.days = 0

    # А также метод run, в котором рыцарь будет сражаться с врагами:
    def run(self):

        # При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
        print(f"{self.name}, на нас напали!")

        # Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
        while self.enemies > 1:
            self.days += 1

            # В процессе сражения количество врагов уменьшается на power текущего рыцаря.
            self.enemies -= self.power

            if self.enemies < 0:
                self.enemies = 0

            # По прошествию 1 дня сражения (1 секунды) выводится строка
            # "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")
            time.sleep(1)

        # После победы над всеми врагами выводится надпись
        # "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")