'''Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)'''

print('Введите трехзначное число')
a = int(input())
summa = 0
num1 =int(a % 10) 
summa += num1

num2 = int(a/ 10 % 10) 
summa += num2

num3 = int(a / 10 /10 % 10) 
summa += num3

print(f'Сумма цифр в числе = {summa}')
