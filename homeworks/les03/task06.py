"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
минимальный и максимальный элементы в сумму не включать. """

import random

array = [random.randint(0, 10) for _ in range(50)]

int_max = -float('inf')
idx_max = 0
int_min = float('inf')
idx_min = 0

for idx, item in enumerate(array):
    if item > int_max:
        int_max, idx_max = item, idx
    if item < int_min:
        int_min, idx_min = item, idx

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

summa = sum(array[idx_min+1:idx_max])
print(summa)
