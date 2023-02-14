''' Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов
второго множества. Затем пользователь вводит сами элементы множеств.
'''

from random import randint

n, m = [int(input()) for _ in range(2)]
first_set = set(randint(1, 100) for _ in range(n))
second_set = set(randint(1, 100) for _ in range(m))
print(first_set, second_set, sep='\n')
print(*sorted(first_set.intersection(second_set)))
