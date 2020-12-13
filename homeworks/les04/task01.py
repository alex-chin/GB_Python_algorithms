"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
первых трех уроков.
Примечание. Идеальным решением будет:

a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

homeworks/les02/task03.py

3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
если введено число 3486, надо вывести 6843. """

import cProfile
import random


def rev(func, n):
    """
    Вызов функции для тестирования и генерация случайного числа
    :param func:
    :param n: количество разрядов
    :return:
    """
    num = random.randint(10 ** (n - 1), 10 ** n)
    return num, func(num)


def reverse1(n):
    """
    Преобразование числа в обратное по порядку входящих в него цифр.
    Рекурсивный подход

    :param n:
    :return:
    """
    nn = n % 10
    rank = n // 10
    if rank == 0:
        return str(nn)
    else:
        return str(nn) + reverse1(rank)


def reverse2(n):
    """
    Преобразование числа в обратное по порядку входящих в него цифр.
    Итерационный подход

    :param n:
    :return:
    """
    result = ''
    while n > 0:
        result += str(n % 10)
        n //= 10
    return result


def reverse3(n):
    """
    Преобразование числа в обратное по порядку входящих в него цифр.
    Подход на основе срезов массивов

    :param n:
    :return:
    """
    return str(n)[-1::-1]


def reverse4(n):
    """
    Преобразование числа в обратное по порядку входящих в него цифр.
    Подход на основе преобразования в строку

    :param n:
    :return:
    """
    buf = str(n)
    result = ''
    for idx in range(len(buf), 0, -1):
        result += buf[idx - 1]
    return result


def test_reverse1(n):
    return rev(reverse1, n)


def test_reverse2(n):
    return rev(reverse2, n)


def test_reverse3(n):
    return rev(reverse3, n)


def test_reverse4(n):
    return rev(reverse4, n)


# print(test_reverse1(500))
# cProfile.run('test_reverse1(10)')
# 21 function calls (12 primitive calls) in 0.000 seconds
#      10/1    0.000    0.000    0.000    0.000 task01.py:32(reverse1)
# cProfile.run('test_reverse1(100)')
# 111 function calls (12 primitive calls) in 0.001 seconds
#    100/1    0.001    0.000    0.001    0.001 task01.py:32(reverse1)
# cProfile.run('test_reverse1(500)')
# 511 function calls (12 primitive calls) in 0.003 seconds
#     500/1    0.003    0.000    0.003    0.003 task01.py:32(reverse1)

# python -m timeit -n 100 -s "import task01" "task01.test3(10)"

# task01.test_reverse1(10)
# 100 loops, best of 5: 7.88 usec per loop
# task01.test_reverse1(100)
# 100 loops, best of 5: 75.4 usec per loop
# task01.test_reverse1(200)
# 100 loops, best of 5: 219 usec per loop
# task01.test_reverse1(500)
# 100 loops, best of 5: 754 usec per loop
# task01.test_reverse1(1000)
# RecursionError: maximum recursion depth exceeded while getting the str of an object
# task01.test_reverse1(1500)
# RecursionError: maximum recursion depth exceeded while getting the str of an object

# task01.test_reverse2(10)
# 100 loops, best of 5: 7.09 usec per loop
# task01.test_reverse2(100)
# 100 loops, best of 5: 67.6 usec per loop
# task01.test_reverse2(200)
# 100 loops, best of 5: 156 usec per loop
# task01.test_reverse2(500)
# 100 loops, best of 5: 645 usec per loop
# task01.test_reverse2(1000)
# 100 loops, best of 5: 3.4 msec per loop
# task01.test_reverse2(1500)
# 100 loops, best of 5: 4.48 msec per loop

# task01.test_reverse3(10)
# 100 loops, best of 5: 3.29 usec per loop
# task01.test_reverse3(100)
# 100 loops, best of 5: 4.37 usec per loop
# task01.test_reverse3(200)
# 100 loops, best of 5: 5.52 usec per loop
# task01.test_reverse3(500)
# 100 loops, best of 5: 11.4 usec per loop
# task01.test_reverse3(1000)
# 100 loops, best of 5: 28.9 usec per loop
# task01.test_reverse3(1500)
# 100 loops, best of 5: 58.6 usec per loop

# task01.test_reverse4(10)
# 100 loops, best of 5: 4.89 usec per loop
# task01.test_reverse4(100)
# 100 loops, best of 5: 16.6 usec per loop
# task01.test_reverse4(200)
# 100 loops, best of 5: 30.6 usec per loop
# task01.test_reverse4(500)
# 100 loops, best of 5: 86.6 usec per loop
# task01.test_reverse4(1000)
# 100 loops, best of 5: 209 usec per loop
# task01.test_reverse4(1500)
# 100 loops, best of 5: 340 usec per loop

# Выводы:
# Реализовать алгоритм возможно различными путями. Преобразование числа является прямой реализацией
# и наиболее затратной. При этом рекурсивный алгоритм(1) имеет еще ограничения по глубине вызовов.
# Итерационный подход(2) имееет линейную сложность вычислений. Нахождение обратного 1500 разрядного числа
# занимает около 4.48 милисек. Если использовать строчное предствление числа (4), то нахождение такого
# числа занимает 340 микросек


