"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

print("Введите число: ")
first_digit = int(input())

if 0 < first_digit < 10:
    secont_digit = first_digit * 11
    third_digit = first_digit * 111
    summary = first_digit + secont_digit + third_digit
    print (f"{first_digit} + {secont_digit} + {third_digit} = {summary}")
else:
    print("Введенное число не соответствует требованиям")