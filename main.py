'''Известно, что количество цифр 2 в конечной строке было в 4 раза меньше, 
чем количество цифр 2 в исходной строке, а сумма значений 
в исходной строке больше суммы значений в конечной строке на 380. 
Сколько цифр 1 было в исходной строке?'''

for zero in range(0, 1001):                   
    for one in range(0, 1001):                
        for two in range(0, 1001):            
            if zero + one + two == 1000:
                n = [0] * zero  + [1] * one + [2] * two
                k = n
                for i in range(len(k)):
                    if k[i] == 0:
                        k[i] = 1
                    elif k[i] == 1:
                        k[i] = 2
                    elif k[i] == 2:
                        k[i] = 0
                if k.count(2) != 0:
                    if (n.count(2) / k.count(2) == 4) and (sum(n) - sum(k) == 380):
                        print(n.count(1))