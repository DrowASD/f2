# Чтение данных
n = int(input())  # Количество чисел в первом списке
first_list = set(int(input()) for _ in range(n))

m = int(input())  # Количество чисел во втором списке
second_list = set(int(input()) for _ in range(m))

# Пересечение множеств
intersection = first_list & second_list

# Вывод результата
print(len(intersection))
