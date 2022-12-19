# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


number = int(input('Введите число: '))
result = 0

while number != 0:
    residual_digit = number % 10
    result = result + residual_digit
    number //= 10
print(result)
        
    
  
