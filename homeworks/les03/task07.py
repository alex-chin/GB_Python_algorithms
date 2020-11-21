"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться. """

import random

array = [random.randint(0, 100) for _ in range(50)]

min1 = float('inf')  # максимальные начальные значения
min2 = float('inf')
for item in array:
    if item < min1:
        min1, min2 = item, min1  # если мин1 изменился мин2=мин1
    elif item < min2:
        min2 = item

print(array)
print(min1, min2)
