class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self): #добавлено для вывода имени в словаре проверяющего класса
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]: #Ошибка исправляется путем добавления оператора [:], без него
                                                     #все обновления происходят в одном цикле, дистанция увеличивается
                                                     # у всех одновременно. Поэтому меньшая скорость (Ник) приходит быстрее участников с большей скоростью.
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
