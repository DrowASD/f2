import math

def factorial_list(n):
    # Находим факториал числа n
    factorial_n = math.factorial(n)
    
    # Создаем список факториалов от factorial_n до 1
    result = [math.factorial(i) for i in range(factorial_n, 0, -1)]
    
    return result

# Пример использования:
n = 3
result = factorial_list(n)
print(result)  # Ожидаемый результат: [720, 120, 24, 6, 2, 1]
