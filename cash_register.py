class CashRegister:
    def __init__(self):
        self.balance = 0

    def top_up(self, amount):
        if amount < 0:
            raise ValueError("Сумма пополнения не может быть отрицательной.")
        self.balance += amount

    def count_1000(self):
        return self.balance // 1000

    def take_away(self, amount):
        if amount < 0:
            raise ValueError("Сумма снятия не может быть отрицательной.")
        if amount > self.balance:
            raise ValueError("Недостаточно денег в кассе.")
        self.balance -= amount
