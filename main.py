'''Операнды арифметического выражения записаны в системе счисления с основаниями 19 и 16:

2x84(19) + 2B3x(16).

В записи чисел переменной x обозначены допустимые в данных системах счисления неизвестные цифры. 
Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 88. 
Для найденного значения x вычислите частное от деления значения арифметического выражения на 88 и 
укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.

16 - 0123456789ABCDEF
19 - 0123456789ABCDEFGH
'''

for x in '0123456789ABCDEF':
    ch1 = int("2" + x + "84", 19)
    v = int("2B3"  + x , 16)
    s = ch1 + v
    if s%88 == 0:
        print(s//88)