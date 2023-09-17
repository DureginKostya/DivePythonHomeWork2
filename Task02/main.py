'''Задание 2:
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное 
строковое представление. Функцию hex используйте для проверки своего результата.'''

number = int(input('Введите целое число в десятичной системе счисления: '))
variable_number = number
number_hex = hex(number)[2:]

DICT_NUMBERS = {10: 'a', 11: 'b',
                12: 'c', 13: 'd',
                14: 'e', 15: 'f'}
RESULT = ''

while variable_number > 0:
    remainder_of_division = variable_number % 16
    if remainder_of_division > 9:
        RESULT = DICT_NUMBERS[remainder_of_division] + RESULT
    else:
        RESULT = str(remainder_of_division) + RESULT
    variable_number //= 16
    
if RESULT == number_hex:
    print(f'Число {number} в шестнадцатеричной системе счисления: {RESULT}')
else:
    print(f'Неверный перевод числа {number} \
в шестнадцатеричную систему счисления: {RESULT} <> {number_hex}')
