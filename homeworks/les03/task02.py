"""2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа. """
import random

array1 = [random.randint(0, 100) for _ in range(50)]
array2 = []
for idx, item in enumerate(array1):
    if item % 2 == 0:
        array2.append(idx)
print(array1)
print(array2)
