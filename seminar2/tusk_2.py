# Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# # чтобы все монетки были повернуты вверх одной и той же стороной. 
# # Выведите минимальное количество монет, которые нужно перевернуть.

import random

coins = random.randint(0, 1)
# 
if coins == 1 :
    print(f'Выпала {coins} монетка, можно перевернуть или попробовать снова )')
else:
        print(f'{coins} штук монет на столе вверх орлом или решкий')
        denushka = [random.randint(0, 1) for i in range(coins)]
        print(denushka)
        orel = sum(denushka)
        if coins == orel or orel == 0:
            print(f'Все монеты лежат либо орлов вверх, либо решкой')
        else:
            print(f'Минимальное количество монет {min(coins-orel, orel)} которое нужно перевернуть.')