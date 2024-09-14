# Импортируем класс CashRegister из файла cash_register.py
from cash_register import CashRegister

kassa = CashRegister()

# Пополняем кассу
kassa.top_up(3000)
print(kassa.balance)       # Ожидается: 3000
print(kassa.count_1000())  # Ожидается: 3 (три тысячи)

# Забираем деньги
kassa.take_away(1000)
print(kassa.balance)       # Ожидается: 2000

# Проверка отрицательных случаев
try:
    kassa.take_away(3000)  # Должна выбросить ошибку: недостаточно денег
except ValueError as e:
    print(e)               # Ожидается: "Недостаточно денег в кассе."

try:
    kassa.top_up(-500)     # Должна выбросить ошибку: отрицательное пополнение
except ValueError as e:
    print(e)               # Ожидается: "Сумма пополнения не может быть отрицательной."

try:
    kassa.take_away(-100)  # Должна выбросить ошибку: отрицательное снятие
except ValueError as e:
    print(e)               # Ожидается: "Сумма снятия не может быть отрицательной."
