# Рекурсивная функция для вывода элементов списка
def print_list_recursive(my_list, index=0):
    # Базовый случай: если индекс выходит за пределы списка
    if index >= len(my_list):
        print("Конец списка")
    else:
        # Вывод текущего элемента
        print(my_list[index])
        # Рекурсивный вызов для следующего элемента
        print_list_recursive(my_list, index + 1)

# Инициализация списка
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Вызов рекурсивной функции
print_list_recursive(my_list)
