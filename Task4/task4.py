# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
import math

n = int(input('Введите число: '))
list = []
for i in range (n):
    list.append (random.randint(-n, n+1))
print(list)

product = math.prod(list)
print(product)

list_txt = open('file.txt', 'w') 
list_txt.write(f'{list}\n')
list_txt.write(f'{product}')