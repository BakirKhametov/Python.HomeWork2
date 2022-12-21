# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Введите число: '))
list = []
for i in range (n):
    list.append (random.randint(-n, n+1))
print(f'Оригинальный список: {list}')
random.shuffle(list)
print(f'Перемешанный список: {list}')