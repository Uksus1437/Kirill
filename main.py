'''Сколько существует шестизначных чисел, делящихся на 5, в которых каждая цифра может встречаться только один раз, 
при этом никакие две чётные и две нечётные цифры не стоят рядом.


0 1 1 2 1
_ _ _ _ _


12634
НЧЧНЧ

НН ЧЧ

6H  H6

replace()
'''

k=0
for a in '123456789':
    for b in'0123456789':
        for c in '0123456789':
            for d in '0123456789':
                for e in '0123456789':
                    for f in '50':
                        w=a+b+c+d+e+f      
                        if w.count('0') <= 1 and w.count('1') <= 1 and w.count('2') <= 1 and w.count('3') <= 1 \
                                and w.count('4') <= 1 and w.count('5') <= 1 and w.count('6') <= 1 and w.count('7') <= 1 \
                                    and w.count('8') <= 1 and w.count('9') <= 1:         
                            w = w.replace('1', 'Н')
                            w = w.replace('3', 'Н')
                            w = w.replace('5', 'Н')
                            w = w.replace('7', 'Н')
                            w = w.replace('9', 'Н')
                            w = w.replace('0', 'Ч')
                            w = w.replace('2', 'Ч')
                            w = w.replace('4', 'Ч')
                            w = w.replace('6', 'Ч')
                            w = w.replace('8', 'Ч')
                            if w.count('ЧЧ')+w.count('НН') == 0:  
                                    k=k+1
print(k)