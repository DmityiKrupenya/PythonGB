# Задача 4 Требуется вывести все целые числа степени двойки (т.е числа вида 2к), 
# не превосходящие числа N.

n = int(input('Введите число N: '))
p = 1 
while p <= n:
    print(p)
    p = p * 2 
