# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

list_1 = [random.randint(-50,50) for _ in range(20)]

print(f'Исходный массив: {list_1}')

minn = int(input("Введите минимальное значение: "))

maxx = int(input("Введите максимальное значение: "))

list_2 = []

if maxx >= minn:

   for i in range(len(list_1)):

      if maxx >= list_1[i] and minn <= list_1[i]:

          list_2.append(i)

   print("Кол-во элементов в диапазоне: ",len(list_2))

   print("Индексы:",list_2)