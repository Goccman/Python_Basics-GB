# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
#
# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint


# поверка на число
def is_number(string):
    if string.isdigit():
        string = int(string)
        return string
    else:
        try:
            float(string)
            string = float(string)
            return string
        except ValueError:
            print("Ввели не число!")
            is_number(input("Введите число: "))


n = is_number(input("Введите количество элементов в массиве: "))
nums_list = [randint(1, n) for _ in range(n)]
print(*nums_list)
num = int(input('Введите искомое число: '))
print(f"Число {num} встречается {nums_list.count(num)} раз")