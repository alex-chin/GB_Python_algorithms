"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random

array = [random.randint(0, 10) for _ in range(50)]
print(array)
max_vector = {}
for item in array:
    max_vector[item] = max_vector.get(item,0) + 1
max_repeat = 0
max_key = None
for key, item in max_vector.items():
    if item > max_repeat:
        max_repeat, max_key = item, key

print(max_vector)
print(max_repeat, max_key)
