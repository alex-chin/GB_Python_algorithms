"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

array = [random.randint(-20, 10) for _ in range(50)]
print(array)
idx_max_min = -1
item_max_min = 0
for idx, item in enumerate(array):
    if item < 0:
        if (item > item_max_min) or idx_max_min == -1:
            item_max_min = item
            idx_max_min = idx
if idx_max_min < 0:
    print('отрицательные числа не найдены')
else:
    print(item_max_min, idx_max_min)
