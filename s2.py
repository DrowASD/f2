# Родительский класс Transport
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    # Метод seating_capacity для отображения вместимости транспорта
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

# Дочерний класс Autobus, наследующий Transport
class Autobus(Transport):
    # Переопределение метода seating_capacity с значением по умолчанию 50
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

# Создание объекта класса Autobus
bus = Autobus("Renaul Logan", 180, 12)

# Вывод вместимости автобуса
print(bus.seating_capacity())  # Вместимость по умолчанию 50
