"""4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры. """

n = int(input('Введите количество :'))
summa = 0
num = 1
for i in range(0, n):
    summa += num
    num *= -0.5
print(summa)
