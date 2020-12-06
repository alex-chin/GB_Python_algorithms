"""Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти."""

import random, sys


def audit(func):
    """
    Первый вариант реализации ДЗ, декоратор который смотрит переменные обвернутой функции и производит вывод
    """

    def wrapper():
        vars_local = func()

        def printer(x, level=0):
            print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
            if hasattr(x, '__iter__'):
                if hasattr(x, 'items'):
                    for key, value in x.items():
                        printer(key, level + 1)
                        printer(value, level + 1)
                elif not isinstance(x, str):
                    for item in x:
                        printer(item, level + 1)

        return printer(vars_local)

    return wrapper


@audit
def min_max_replace_1():
    """В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

    # list(random.randint(2000, 3000) for _ in range(0, 10))
    array = [2225, 2043, 2790, 2763, 2556, 2310, 2199, 2976, 2847, 2382]
    print(array)

    min_element_index = 0
    min_element = 3000
    max_element_index = 0
    max_element = 0
    current_index = 0

    for element in array:
        if min_element > element:
            min_element = element
            min_element_index = current_index

        if max_element < element:
            max_element = element
            max_element_index = current_index

        current_index += 1

    array[min_element_index], array[max_element_index] = max_element, min_element
    print(array)

    return locals()


# type = <class 'list'>, size = 72, object = [{'array': [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382], 'min_element_index': 1, 'min_element': 2043, 'max_element_index': 7, 'max_element': 2976, 'current_index': 10, 'element': 2382}]
# 	 type = <class 'dict'>, size = 368, object = {'array': [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382], 'min_element_index': 1, 'min_element': 2043, 'max_element_index': 7, 'max_element': 2976, 'current_index': 10, 'element': 2382}
# 		 type = <class 'str'>, size = 54, object = array
# 		 type = <class 'list'>, size = 144, object = [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382]
# 			 type = <class 'int'>, size = 28, object = 2225
# 			 type = <class 'int'>, size = 28, object = 2976
# 			 type = <class 'int'>, size = 28, object = 2790
# 			 type = <class 'int'>, size = 28, object = 2763
# 			 type = <class 'int'>, size = 28, object = 2556
# 			 type = <class 'int'>, size = 28, object = 2310
# 			 type = <class 'int'>, size = 28, object = 2199
# 			 type = <class 'int'>, size = 28, object = 2043
# 			 type = <class 'int'>, size = 28, object = 2847
# 			 type = <class 'int'>, size = 28, object = 2382
# 		 type = <class 'str'>, size = 66, object = min_element_index
# 		 type = <class 'int'>, size = 28, object = 1
# 		 type = <class 'str'>, size = 60, object = min_element
# 		 type = <class 'int'>, size = 28, object = 2043
# 		 type = <class 'str'>, size = 66, object = max_element_index
# 		 type = <class 'int'>, size = 28, object = 7
# 		 type = <class 'str'>, size = 60, object = max_element
# 		 type = <class 'int'>, size = 28, object = 2976
# 		 type = <class 'str'>, size = 62, object = current_index
# 		 type = <class 'int'>, size = 28, object = 10
# 		 type = <class 'str'>, size = 56, object = element
# 		 type = <class 'int'>, size = 28, object = 2382

@audit
def min_max_replace_2():
    """В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

    # list(random.randint(2000, 3000) for _ in range(0, 10))
    array = [2225, 2043, 2790, 2763, 2556, 2310, 2199, 2976, 2847, 2382]
    print(array)

    min_element = min(array)
    max_element = max(array)

    min_element_index = array.index(min_element)
    max_element_index = array.index(max_element)

    # Можно вместо переменных max и min вставить вызовы, но я хотел сохранить некоторое кол-во переменных
    array[min_element_index], array[max_element_index] = max_element, min_element
    print(array)

    return locals()


# type = <class 'dict'>, size = 240, object = {'array': [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382], 'min_element': 2043, 'max_element': 2976, 'min_element_index': 1, 'max_element_index': 7}
# 	 type = <class 'str'>, size = 54, object = array
# 	 type = <class 'list'>, size = 144, object = [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382]
# 		 type = <class 'int'>, size = 28, object = 2225
# 		 type = <class 'int'>, size = 28, object = 2976
# 		 type = <class 'int'>, size = 28, object = 2790
# 		 type = <class 'int'>, size = 28, object = 2763
# 		 type = <class 'int'>, size = 28, object = 2556
# 		 type = <class 'int'>, size = 28, object = 2310
# 		 type = <class 'int'>, size = 28, object = 2199
# 		 type = <class 'int'>, size = 28, object = 2043
# 		 type = <class 'int'>, size = 28, object = 2847
# 		 type = <class 'int'>, size = 28, object = 2382
# 	 type = <class 'str'>, size = 60, object = min_element
# 	 type = <class 'int'>, size = 28, object = 2043
# 	 type = <class 'str'>, size = 60, object = max_element
# 	 type = <class 'int'>, size = 28, object = 2976
# 	 type = <class 'str'>, size = 66, object = min_element_index
# 	 type = <class 'int'>, size = 28, object = 1
# 	 type = <class 'str'>, size = 66, object = max_element_index
# 	 type = <class 'int'>, size = 28, object = 7

@audit
def min_max_replace_3():
    """В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

    # list(random.randint(2000, 3000) for _ in range(0, 10))
    array = [2225, 2043, 2790, 2763, 2556, 2310, 2199, 2976, 2847, 2382]
    print(array)

    # __getitem__ реализует возвращение по индексу
    i, j = [
        func(range(len(array)), key=array.__getitem__)
        for func
        in [min, max]
    ]

    # второй вариант с выражением-генератором
    # i, j = [
    #     i
    #     for i
    #     in range(len(array))
    #     if array[i] == min(array) or array[i] == max(array)
    # ]

    array[i], array[j] = array[j], array[i]

    print(array)
    return locals()


# type = <class 'dict'>, size = 240, object = {'i': 1, 'j': 7, 'array': [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382]}
# 	 type = <class 'str'>, size = 50, object = i
# 	 type = <class 'int'>, size = 28, object = 1
# 	 type = <class 'str'>, size = 50, object = j
# 	 type = <class 'int'>, size = 28, object = 7
# 	 type = <class 'str'>, size = 54, object = array
# 	 type = <class 'list'>, size = 144, object = [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382]
# 		 type = <class 'int'>, size = 28, object = 2225
# 		 type = <class 'int'>, size = 28, object = 2976
# 		 type = <class 'int'>, size = 28, object = 2790
# 		 type = <class 'int'>, size = 28, object = 2763
# 		 type = <class 'int'>, size = 28, object = 2556
# 		 type = <class 'int'>, size = 28, object = 2310
# 		 type = <class 'int'>, size = 28, object = 2199
# 		 type = <class 'int'>, size = 28, object = 2043
# 		 type = <class 'int'>, size = 28, object = 2847
# 		 type = <class 'int'>, size = 28, object = 2382

# type = <class 'dict'>, size = 240, object = {'i': 1, 'j': 7, 'array': [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382]}
# 	 type = <class 'str'>, size = 50, object = i
# 	 type = <class 'int'>, size = 28, object = 1
# 	 type = <class 'str'>, size = 50, object = j
# 	 type = <class 'int'>, size = 28, object = 7
# 	 type = <class 'str'>, size = 54, object = array
# 	 type = <class 'list'>, size = 144, object = [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382]
# 		 type = <class 'int'>, size = 28, object = 2225
# 		 type = <class 'int'>, size = 28, object = 2976
# 		 type = <class 'int'>, size = 28, object = 2790
# 		 type = <class 'int'>, size = 28, object = 2763
# 		 type = <class 'int'>, size = 28, object = 2556
# 		 type = <class 'int'>, size = 28, object = 2310
# 		 type = <class 'int'>, size = 28, object = 2199
# 		 type = <class 'int'>, size = 28, object = 2043
# 		 type = <class 'int'>, size = 28, object = 2847
# 		 type = <class 'int'>, size = 28, object = 2382

@audit
def min_max_replace_4():
    """В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

    array = [2225, 2043, 2790, 2763, 2556, 2310, 2199, 2976, 2847, 2382]
    print(array)

    array[array.index(max(array))], array[array.index(min(array))] = min(array), max(array)
    print(array)

    return locals()


# type = <class 'dict'>, size = 240, object = {'array': [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382]}
# 	 type = <class 'str'>, size = 54, object = array
# 	 type = <class 'list'>, size = 144, object = [2225, 2976, 2790, 2763, 2556, 2310, 2199, 2043, 2847, 2382]
# 		 type = <class 'int'>, size = 28, object = 2225
# 		 type = <class 'int'>, size = 28, object = 2976
# 		 type = <class 'int'>, size = 28, object = 2790
# 		 type = <class 'int'>, size = 28, object = 2763
# 		 type = <class 'int'>, size = 28, object = 2556
# 		 type = <class 'int'>, size = 28, object = 2310
# 		 type = <class 'int'>, size = 28, object = 2199
# 		 type = <class 'int'>, size = 28, object = 2043
# 		 type = <class 'int'>, size = 28, object = 2847
# 		 type = <class 'int'>, size = 28, object = 2382


# min_max_replace_1()
# min_max_replace_2()
# min_max_replace_3()
min_max_replace_4()


"""
Вывод
В первой реализации я взял и слегка отредактировал версию из 3го урока своего ДЗ, она оказалось не только плохо написана
а еще и много "кушает" памяти.
В второй реализации я сохранил еще некоторые переменные, убрал циклы и воспользовался (тоже не без циклов но уже 
под капотом) встроенными функция языка и результат по памяти стал лучше
В третьей реализации я постарался использовать выражение-генератор, сначала не получалось (да и в целом не получилось 
на нем одном остановится) в итоге я пришел к нескольким решениями, но как бы не извращался с выражением итог по памяти 
всегда был одинаков
Четвертую реализацию я добавил специально посмотреть что будет если постараться по максимуму сократить кол-во строк кода
- оказалось оно напрямую зависит =) в итоге я получил самый лучший вариант по использованию памяти из своих "исследований"
но там одно но, данный алгоритм не отвечает критерию - массовость, если первое число в массиве будет максимальным, тогда
нужно менять выражение местами...
В итоге все таки вариант с выражением-генератором можно считать лучшим именно в моих решениях
"""