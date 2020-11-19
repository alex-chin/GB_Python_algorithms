"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

array = [random.randint(0, 100) for _ in range(50)]

min_num = float('inf')
min_idx = 0
max_num = 0
max_idx = 0

for idx, item in enumerate(array):
    if item > max_num:
        max_num, max_idx = item, idx
    if item < min_num:
        min_num, min_idx = item, idx
print(array)
print(max_num, max_idx)
print(min_num, min_idx)
array[max_idx], array[min_idx] = array[min_idx], array[max_idx]
print(array)