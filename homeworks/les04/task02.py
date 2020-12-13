"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и
попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:
sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
Примечание по профилированию кода: для получения достоверных результатов при замере времени
необходимо исключить/заменить функции print() и input() в анализируемом коде.

С ними вы будете замерять время вывода данных в терминал и время, потраченное пользователем,
на ввод данных, а не быстродействие самого алгоритма.
"""
import cProfile


def bolter(num):
    n = 10 ** 6

    def is_prime(n):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n

    count = 0
    for elem in range(2, n):
        if is_prime(elem):
            count += 1
            if count == num:
                break
    return elem


def sieve(num):
    n = 10 ** 6
    si = [i for i in range(n)]
    si[1] = 0
    for i in range(2, n):
        if si[i] != 0:
            j = i * 2
            while j < n:
                si[j] = 0
                j += i
    count = 0
    for elem in si:
        if elem != 0:
            count += 1
            if count == num:
                break
    return elem



# print(sieve(2))
# print(sieve(4))
# print(sieve(5))
# print(sieve(1))
#
# print(bolter(2))
# print(bolter(4))
# print(bolter(5))
# print(bolter(1))


# print(sieve(100))


# python -m timeit -n 100 -s "import task02" "task02.bolter(10)"

# task02.bolter(10)
# 100 loops, best of 5: 10.4 usec per loop
# task02.bolter(100)
# 100 loops, best of 5: 350 usec per loop
# task02.bolter(500)
# 100 loops, best of 5: 4.42 msec per loop
# task02.bolter(1000)
# 100 loops, best of 5: 11.9 msec per loop

# task02.sieve(10)
# 100 loops, best of 5: 298 usec per loop
# task02.sieve(100)
# 100 loops, best of 5: 375 usec per loop

# cProfile.run('sieve(50)')
#         1    1.063    1.063    1.353    1.353 task02.py:46(sieve)
#         1    0.290    0.290    0.290    0.290 task02.py:48(<listcomp>)

# Выводы: Метод прямого поиска простых чисел имеет квадратичную сложность. Метод «Решето Эратосфена» обладает такой
# же сложнстью, однако больше подходит для поиска множества простых. Поэтому требует большего времени на подготовку
# - генерацию "решета"


