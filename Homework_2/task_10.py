# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное количество
# монет, которые нужно перевернуть.
#
# Пример:
# 5 -> 1 0 1 1 0
# 2

from random import randint

n = int(input("Введите количество монеток: "))
coins = []
for i in range(n):
    coins.append(randint(0, 1))
print(coins)

zero = coins.count(0)
one = coins.count(1)

if zero < one:
    print(f"Нужно перевернуть {zero} монет.")
elif zero == one:
    print(f"Количество монет одинаковое и равно {zero} - можно перевернуть любую сторону")
else:
    print(f"Нужно перевернуть {one} монет.")
