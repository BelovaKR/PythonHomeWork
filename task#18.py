# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# пример
# 5
# 1 2 3 4 5
# 6
# -> 5

print('Введите кол-во элементов массива')
size = int(input())

arr = [int(input('Введите значение массива: ')) for _ in range(size)]

x = int(input('Введите значение x: '))

res = arr[0]
for i in arr:
    if abs(i - x) < abs(res - x):
        res = i

print(res)
print(f'Размерность массива: {size}')
print(f'Исходный массив: {arr}')
print(f"Искомое значение: {x}")
print(f'Самый близкий по величине элемент: {res}')