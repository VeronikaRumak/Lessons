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


# Создайте объект класса House с произвольным названием и количеством этажей.
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызовите метод go_to у этого объекта с произвольным числом.
h1.go_to(5)
h2.go_to(10)


