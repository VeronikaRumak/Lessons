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


# Создайте объект класса House с произвольным названием и количеством этажей.
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

# Вызовите метод go_to у этого объекта с произвольным числом.
# h1.go_to(5)
# h2.go_to(10)


