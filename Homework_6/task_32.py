'''Задача 32:
Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не
больше заданного максимума)
'''

from random import randint


def create_list(x):
    my_list = []
    for i in range(x):
        my_list.append(randint(0, 20))
    return my_list


def find_indexes(list_1, min_number, max_number):
    indexes_list = []
    for i in range(len(list_1)):
        if min_number <= list_1[i] <= max_number:
            indexes_list.append(i)
    return indexes_list


num_list = create_list(int(input('Введите размер массива: ')))
print(num_list)
min_number = int(input('Введите минимум диапазона: '))
max_number = int(input('Введите максимум диапазона: '))
print(find_indexes(num_list, min_number, max_number))
