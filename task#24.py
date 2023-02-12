# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# | 4 -> 1 2 3 4
# 9 |

import random
print('Введите кол-во количество кустов')
size = int(input())

berries = [random.randint(1,20) for _ in range(size)]

max = 0

for i in range(size):
    summa = sum(berries[i:i+3])
    if max < summa:
        max = summa
        i += 1

if berries[0] + berries[-1] + berries[-2] > max:
	max = berries[0] + berries[-1] + berries[-2]
if berries[0] + berries[1] + berries[-1] > max:
	max = berries[0] + berries[1] + berries[-1]

print(f'Количество ягод на кустах: {berries}')
print(f'Максимальное количество ягод, которое может собрать собирающий модуль за один заход: {max}')        