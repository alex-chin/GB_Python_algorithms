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
import random


def rev(func, n):
    num = random.randint(10 ** (n - 1), 10 ** n)
    return num, func(num)


def reverse1(n):
    nn = n % 10
    rank = n // 10
    if rank == 0:
        return str(nn)
    else:
        return str(nn) + reverse1(rank)


def reverse2(n):
    result = ''
    while n > 0:
        result += str(n % 10)
        n //= 10
    return result


def reverse3(n):
    return str(n)[-1::-1]


def test1(n):
    rev(reverse1, n)


def test2(n):
    rev(reverse2, n)


def test3(n):
    rev(reverse3, n)

# print(rev(reverse1, 10))
# print(rev(reverse2, 10))
# print(rev(reverse3, 10))

# python -m timeit -n 100 -s "import task01" "task01.rev(reverse1, 10)"
# python -m timeit -n 100 -s "import task01" "task01.test3(500)"
