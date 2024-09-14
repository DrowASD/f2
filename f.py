class Turtle:
    def __init__(self, x=0, y=0, s=1):
        """Инициализация начальных координат (x, y) и шага s."""
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        """Перемещает черепашку вверх, увеличивая y на s."""
        self.y += self.s

    def go_down(self):
        """Перемещает черепашку вниз, уменьшая y на s."""
        self.y -= self.s

    def go_left(self):
        """Перемещает черепашку влево, уменьшая x на s."""
        self.x -= self.s

    def go_right(self):
        """Перемещает черепашку вправо, увеличивая x на s."""
        self.x += self.s

    def evolve(self):
        """Увеличивает количество шагов черепашки на 1."""
        self.s += 1

    def degrade(self):
        """Уменьшает количество шагов черепашки на 1 или выкидывает ошибку, если шаг ≤ 0."""
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Шаг не может быть меньше или равен 0.")

    def count_moves(self, x2, y2):
        """Возвращает минимальное количество шагов для достижения точки (x2, y2)."""
        dist_x = abs(self.x - x2)
        dist_y = abs(self.y - y2)
        # Минимальное количество шагов
        steps_x = -(-dist_x // self.s)  # То же, что и math.ceil(dist_x / self.s)
        steps_y = -(-dist_y // self.s)  # То же, что и math.ceil(dist_y / self.s)
        return max(steps_x, steps_y)

# Пример использования:
turtle = Turtle()   # Начальная позиция (0, 0) и шаг 1
turtle.go_up()      # Позиция (0, 1)
turtle.go_right()   # Позиция (1, 1)
turtle.evolve()     # Шаг увеличивается до 2
print(turtle.count_moves(5, 5))  # Минимальное количество шагов для достижения (5, 5)
