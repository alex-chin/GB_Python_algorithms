"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""
from collections import deque

rang = tuple('0123456789ABCDEF')  # словарь преобразования разрядов
# a = deque('1F1')
a = deque(input("Введите а:").upper())
# b = deque('23BC6')
b = deque(input("Введите b:").upper())
summa = deque()  # сумма
a.extendleft('0' * (max(len(a), len(b)) - len(a)))  # выравнивание нулями
print(' ', ''.join(a))
b.extendleft('0' * (max(len(a), len(b)) - len(b)))  # выравнивание нулями
print('+', ''.join(b))
print('-' * 5)
shift = 0
for i in range(len(a)):  # контроль по 1 слагаемому, так как выровнены
    s = rang.index(a.pop()) + rang.index(b.pop()) + shift  # сумматор + перенос
    summa.extendleft([rang[s % 16]])  # запись в разрад со сдвигом
    shift = s // 16  # вычисление переноса
print(' ', ''.join(summa))

