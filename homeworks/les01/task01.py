"""
1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый
сдвиг вправо и влево на два знака.
"""

x1 = 5
x2 = 6

b1 = x1 | x2
b2 = x1 & x2
b3 = x1 ^ x2
b4 = ~x1
b5 = x1 >> 2
b6 = x1 << 2

print(f'x1={x1:0>8b} x2={x2:0>8b}, x1 ИЛИ  x2 = {b1:0>8b}')
print(f'x1={x1:0>8b} x2={x2:0>8b}, x1  И   x2 = {b2:0>8b}')
print(f'x1={x1:0>8b} x2={x2:0>8b}, x1 иИЛИ x2 = {b3:0>8b}')
print(f'x1={x1:0>8b},        НЕ x1 = {b4:0>8b}')
print(f'x1={x1:0>8b}, СДВИГ ПРВ x1 = {b5:0>8b}')
print(f'x1={x1:0>8b}, СДВИГ ЛЕВ x1 = {b6:0>8b}')

