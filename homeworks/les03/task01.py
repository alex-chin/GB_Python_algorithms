"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов. """
for num in range(2, 100):
    is_multi = False
    for multi in range(2, 10):
        if num % multi == 0:
            print(f' {multi}', end='')
            is_multi = True
            break
    if is_multi:
        print()
        print(num)
