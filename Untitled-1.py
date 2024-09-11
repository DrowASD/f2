def power_and_multiply(num):
    """
    Вычисляет результат по заданной формуле, учитывая особенности числа.

    Args:
        num: Целое положительное число.

    Returns:
        Результат вычисления.

    Raises:
        ValueError: Если вхождение данных некорректно или если происходит деление на ноль.
    """

    if num <= 0:
        raise ValueError("Число должно быть положительным")

    # Извлечение последних трех цифр числа
    hundreds = (num // 100) % 10
    tens = (num // 10) % 10
    units = num % 10

    # Проверяем на деление на ноль
    divisor = (tens * 10 - units)
    if divisor == 0:
        raise ValueError("Деление на ноль невозможно")

    # Проверка корректности возведения в степень
    if units == 0 and tens == 0:
        raise ValueError("Невозможно возвести в степень")

    # Расчет результата
    result = (tens ** units) * hundreds
    result /= divisor

    return result

# Пример использования
num = 46275
print(power_and_multiply(num))

# https://github.com/DrowASD/St4p2