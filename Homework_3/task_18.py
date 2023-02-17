# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5


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
            return is_number(input("Введите число: "))


n = int(is_number(input("Введите количество элементов в массиве: ")))
numbers = tuple(randint(1, n) for _ in range(n))
print(*numbers)
num = int(input('Введите искомое число: '))
mod = 0
flag = False
for _ in range(len(set(numbers))):
    for i in set(numbers):
        if i == num - mod or i == num + mod:
            print(f"Для числа {num} ближайшим элементом является {i}")
            flag = True
            break
    if flag:
        break
    mod += 1




