'''Задание 3:
Напишите программу, которая принимает две строки вида “a/b” - дробь
с числителем и знаменателем. Программа должна возвращать сумму и 
произведение * дробей. Для проверки своего кода используйте модуль fractions.'''

import fractions
import math

fr_number_first = input('Введите первое дробное число (a/b): ')
fr_number_second = input('Введите второе дробное число (a/b): ')

fr_first = list(map(int, fr_number_first.split('/')))
fr_second = list(map(int, fr_number_second.split('/')))

if fr_first[1] == fr_second[1]:
    numerator_sum = fr_first[0] + fr_second[0]
    denominator_sum = fr_first[1]
else:
    numerator_sum = fr_first[0] * fr_second[1] + fr_first[1] * fr_second[0]
    denominator_sum = fr_first[1] * fr_second[1]
if float(numerator_sum / denominator_sum) == float(fractions.Fraction(fr_number_first) +
                                                   fractions.Fraction(fr_number_second)):
    gcd_sum = math.gcd(numerator_sum, denominator_sum)
    if numerator_sum % denominator_sum == 0:
        print(f'Результат сложения: {numerator_sum // denominator_sum}')
    elif gcd_sum != 1:
        numerator_sum //= gcd_sum
        denominator_sum //= gcd_sum
        print(f'Результат сложения: {numerator_sum}/{denominator_sum}')
    else:
        print(f'Результат сложения: {numerator_sum}/{denominator_sum}')
else:
    print('Сложение дробей рассчитано неверно')

numerator_multiply = fr_first[0] * fr_second[0]
denominator_multiply = fr_first[1] * fr_second[1]
if float(numerator_multiply / denominator_multiply) == float(fractions.Fraction(fr_number_first) *
                                                             fractions.Fraction(fr_number_second)):
    gcd_multiply = math.gcd(numerator_multiply, denominator_multiply)
    if numerator_multiply % denominator_multiply == 0:
        print(
            f'Результат умножения: {numerator_multiply // denominator_multiply}')
    elif gcd_multiply != 1:
        numerator_multiply //= gcd_multiply
        denominator_multiply //= gcd_multiply
        print(
            f'Результат сложения: {numerator_multiply}/{denominator_multiply}')
    else:
        print(
            f'Результат сложения: {numerator_multiply}/{denominator_multiply}')
else:
    print('Умножение дробей рассчитано неверно')
