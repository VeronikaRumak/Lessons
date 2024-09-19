

# Изменения в классе Runner:
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        # Появился атрибут speed для определения скорости бегуна.
        self.speed = speed

    # Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    # Метод __eq__ для сравнивания имён бегунов.
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


# Класс Tournament представляет собой класс соревнований,
# где есть дистанция, которую нужно пробежать и список участников.
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    # Также присутствует метод start, который реализует логику бега по предложенной дистанции.
    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name  # Сохраняем имя бегуна с помощью .name
                    place += 1
                    self.participants.remove(participant)

                    break   # Выход из цикла после удаления участника

        return finishers




