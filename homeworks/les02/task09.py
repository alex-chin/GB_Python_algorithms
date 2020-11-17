"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и
сумму его цифр. """

max_sum = 0
max_n = 0
while True:
    n1 = int(input("Введите число (0-конец) :"))
    if n1 == 0:
        break
    n = n1
    summa = 0
    while n != 0:
        summa += n % 10
        n //= 10
    print(summa)
    if summa > max_sum:
        max_sum = summa
        max_n = n1
print(max_n, max_sum)
