# Задача 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

def Task_1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for elem in a:
        if elem < 5:
            print(elem)



##################################################################################
# Задача 2
# Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

def Task_2():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    result = []
    for elem in a:
        if elem in b:
            result.append(elem)

    print(result)


##################################################################################
# Задача 3
# Отсортируйте словарь по значению в порядке возрастания и убывания.

def Task_3():
    import operator

    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print('Оригинальный словарь: ',d)
    sorted_d = sorted(d.items(), key=operator.itemgetter(0))
    print('Словарь в порядке возрастания по значению: ',sorted_d)
    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(0),reverse=True))
    print('Словарь в порядке убывания по значению: ',sorted_d)


##################################################################################
# Задача 4
# Напишите программу для слияния нескольких словарей в один.

def Task_4():
    dict_a = {1:10, 2:20}
    dict_b = {3:30, 4:40}
    dict_c = {5:50, 6:60}

    result = {}

    for d in (dict_a, dict_b, dict_c):
        result.update(d)

    print(result)

##################################################################################
# Задача 5
# Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

def Task_5():
    my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

    print(sorted(my_dict.values())[-3:])

##################################################################################
# Задача 6
# Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.

def Task_6():
    print(int('ABC', 16))

##################################################################################
# Задача 7
# Нужно вывести первые n строк треугольника Паскаля.
# В этом треугольнике на вершине и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных над ним чисел.

def Task_7(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]

# Task_7(6)

##################################################################################
# Задача 8
# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

def Task_8(string):
    return string == string[::-1]

#print(Task_8('abba'))

##################################################################################
# Задача 9
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

def Task_9(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')


#Task_9(1234565)

##################################################################################
# Задача 10
# Вы принимаете от пользователя последовательность чисел, разделённых запятой.
# Составьте список и кортеж с этими числами.

def Task_10():
    try:
        values = input('Введите числа через запятую: ')
        ints_as_strings = values.split(',')
        ints = map(int, ints_as_strings)
        lst = list(ints)
        tup = tuple(lst)
        print('Список:', lst)
        print('Кортеж:', tup)

    except:
        print("Вы ввели числа через пробел")

#Task_10()

# :) or :| or :(