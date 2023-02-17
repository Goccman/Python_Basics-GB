'''Задача 26
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

Пример:
A = 3; B = 5 -> 243 (3**5)
A = 2; B = 3 -> 8
'''


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


def a_pow_b(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return a * a_pow_b(a, b - 1)

number = int(is_number(input('Введите число: ')))
power = int(is_number(input('Введите значение степени: ')))
print(a_pow_b(number, power))
