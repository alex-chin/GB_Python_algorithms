"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов. """
a = [0] * 8
for item in range(2, 100):
    for multi in range(2, 10):
        if item % multi == 0:
            a[multi - 2] += 1

for idx, item in enumerate(a):
    print(f'{idx + 2}: {item}')
