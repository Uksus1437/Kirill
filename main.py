'''Автомат обрабатывает натуральное число N по следующему алгоритму:

1. Строится двоичная запись числа N без ведущих нулей.
2. Если в полученной записи единиц больше, чем нулей, то справа приписывается единица. 
Если нулей больше или нулей и единиц поровну, справа приписывается ноль.
3. Полученное число переводится в десятичную запись и выводится на экран. 

Какое наименьшее число, превышающее 80, может получиться в результате работы автомата?
'''

a = []

for n in range(1,100):
    r=bin(n)[2:]
    if r.count('1')>r.count('0'):
        r=r+'1'
    if r.count('0')>=r.count('1'):
        r=r+'0'
    
    r=int(r,2)
    if r >80:
        print(r)
    
    
        