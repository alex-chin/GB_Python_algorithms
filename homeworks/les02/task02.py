"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
n = int(input('Введите число :'))
n_odd = 0
n_even = 0
while n > 0:
    if (n % 10) % 2 == 0:
        n_even += 1
    else:
        n_odd += 1
    n //= 10
print(f'четных-{n_even}, нечетных-{n_odd}')
