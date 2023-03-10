# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств. 

# | 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12 

print('Введите кол-во элементов первого множества')
size_1 = int(input())

new_list_1 = [int(input('Введите значене первого множества: ')) for _ in range(size_1)]

print('Введите кол-во элементов второго множества')
size_2 = int(input())

new_list_2 = [int(input('Введите значене второго множества: ')) for _ in range(size_2)]

print(f'Первое множество :{new_list_1}')
print(f'Второе множество :{new_list_2}')

colors_1 = set(new_list_1)
colors_2 = set(new_list_2)

rez = colors_1.intersection(colors_2)
print(f'Числа встресающиеся в обоих наборах : {sorted(rez)}')