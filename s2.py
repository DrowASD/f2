class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного транспортного средства {self.name}: {capacity} пассажиров"

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self):
        # Переопределяем метод с заданным значением по умолчанию
        return f"Вместимость одного автобуса {self.name}: 50 пассажиров"

# Создаем экземпляр класса Autobus
bus = Autobus("Renault Logan", 120, 10)

# Вызываем метод seating_capacity без аргумента
print(bus.seating_capacity())