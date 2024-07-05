print()     # Отступ


# Создайте класс House.
class House:
    # Внутри класса House определите метод __init__,
    # в который передадите название и кол-во этажей
    def __init__(self, name, number_of_floors):
        # Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors,
        # присвойте им переданные значения.
        self.name = name
        self.number_of_floors = number_of_floors

    # Создайте метод go_to с параметром new_floor и
    # напишите логику внутри него на основе описания задачи.
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    # Необходимо дополнить класс House следующими специальными методами:
    # __len__(self) - должен возвращать кол - во этажей здания self.number_of_floors.
    def __len__(self):
        return self.number_of_floors

    # __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # __eq__(self, other) - должен возвращать True,
    # если количество этажей одинаковое у self и у other.
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            return 'Ошибка! Введите кол - во этажей'

    # Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=)
    # должны присутствовать в классе и возвращать результаты сравнения
    # по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            return 'Ошибка! Введите кол - во этажей'

    # __add__(self, value) - увеличивает кол-во этажей на переданное значение value,
    # возвращает сам объект self.
    def __add__(self, other):
        self.number_of_floors += other
        return self

    # __radd__(self, value), __iadd__(self, value) - работают так же
    # как и __add__ (возвращают результат его вызова).
    def __radd__(self, other):
        self.__add__(other)
        return self

    def __iadd__(self, other):
        self.__add__(other)
        return self


# Создайте объект класса House с произвольным названием и количеством этажей.
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __eq__
print(h1 == h2)

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

# __len__
# print(len(h1))
# print(len(h2))

# Вызовите метод go_to у этого объекта с произвольным числом.
# h1.go_to(5)
# h2.go_to(10)


