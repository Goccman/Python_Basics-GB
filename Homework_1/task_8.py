# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить
# шоколадку на два прямоугольника).
#
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no


n = int(input("Количество долек в длину: "))
m = int(input("Количество долек в ширину: "))
k = int(input("Количество долек, которые нужно отломить: "))
if (n == k or k % n == 0 and k <= n * m - n) or (m == k or k % m == 0 and k <= n * m - m):
    print('\nyes')
else:
    print('\nno')
