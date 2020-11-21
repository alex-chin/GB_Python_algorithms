"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

matrix = [[random.randint(0, 100) for _ in range(5)] for _ in range(6)]
min_elem = float('inf')
min_col = []
# print(matrix)

for col in range(0, len(matrix[0])):
    for line in matrix:
        if line[col] < min_elem:  # анализ элемента в столбце
            min_elem = line[col]
    min_col.append(min_elem)  # формирование вектора мин
    min_elem = float('inf')
# print(min_col)
max_elem = -float('inf')
for elem in min_col: # поиск макс в векторе
    if elem > max_elem:
        max_elem = elem
print(max_elem)
