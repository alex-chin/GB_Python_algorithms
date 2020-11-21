"""8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
матрицу. """

mat = []
line = []
summa = 0
for _ in range(0, 4):
    for _ in range(0, 4):
        item = int(input("Введите число :"))
        line.append(item)
        summa += item
    line.append(summa)
    mat.append(line[:])  # копирование строки
    print(f'============ {summa}')
    line = []
    summa = 0
for line in mat:
    print(f'{line[0]:4} {line[1]:4} {line[2]:4} {line[3]:4} {line[4]:4}')
