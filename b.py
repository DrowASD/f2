import random

# Функция для создания матрицы размером rows x cols, заполненной случайными числами
def generate_matrix(rows, cols):
    return [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

# Функция для сложения двух матриц
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result_matrix

# Генерация двух матриц 10x10
matrix_1 = generate_matrix(10, 10)
matrix_2 = generate_matrix(10, 10)

# Сложение двух матриц
matrix_3 = add_matrices(matrix_1, matrix_2)

# Вывод результатов
print("Matrix 1:")
for row in matrix_1:
    print(row)

print("\nMatrix 2:")
for row in matrix_2:
    print(row)

print("\nMatrix 3 (Matrix 1 + Matrix 2):")
for row in matrix_3:
    print(row)
