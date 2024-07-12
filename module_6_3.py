print()     # Отступ


# Необходимо написать 3 класса:

# Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
class Horse:
    def __init__(self):
        # x_distance = 0 - пройденный путь.
        self.x_distance = 0

        # sound = 'Frrr' - звук, который издаёт лошадь.
        self.sound = 'Frrr'
        super().__init__()
        
    # И методами:
    # run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.
    def run(self, dx):
        self.x_distance += dx


# Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
class Eagle:
    def __init__(self):
        # y_distance = 0 - высота полёта
        self.y_distance = 0

        # sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
        self.sound = 'I train, eat, sleep, and repeat'

    # И методами:
    # fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.
    def fly(self, dy):
        self.y_distance += dy


# Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
# Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    # Также обладает методами:

    # move(self, dx, dy) - где dx и dy изменения дистанции.
    def move(self, dx, dy):
        # В этом методе должны запускаться наследованные методы run и fly соответственно.
        self.run(dx)
        self.fly(dy)

    # get_pos(self) возвращает текущее положение пегаса в виде кортежа -
    # (x_distance, y_distance) в том же порядке.
    def get_pos(self):
        return self.x_distance, self.y_distance

    # voice - который печатает значение унаследованного атрибута sound.
    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()