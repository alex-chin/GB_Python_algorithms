"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима).
"""

# HeapSort - пирамидальная сортровка

import random

m = 20
n = 4

array = [i for i in range(n, n + 1 + 2 * m)]
random.shuffle(array)
print(array)


def heap_bin(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        heap_bin(array, n, largest)


def heap_sort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heap_bin(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap_bin(array, i, 0)


heap_sort(array)
print(array)
print("Длина массива =", len(array))
print(" Медиана массива =", array[len(array) // 2])
