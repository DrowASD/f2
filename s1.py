# Родительский класс Transport
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    # Метод для вывода информации об объекте
    def display_info(self):
        return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"

# Дочерний класс Autobus, наследующий Transport
class Autobus(Transport):
    pass  # Наследуем все, что есть в родительском классе

# Создание объекта класса Autobus
bus = Autobus("Renaul Logan", 180, 12)

# Вывод информации об объекте
print(bus.display_info())
