# Чтение данных
numbers = input().split()  # Разделяем строку по пробелам

# Множество для хранения уже встреченных чисел
seen = set()

# Обработка каждого числа
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
