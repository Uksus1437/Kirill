ip = list(map(int, '205.182.128.0 '.split('.')))
print(f'{bin(ip[0])[2:].zfill(8)}.{bin(ip[1])[2:].zfill(8)}.{bin(ip[2])[2:].zfill(8)}.{bin(ip[3])[2:].zfill(8)}')


ip = list(map(int, '255.255.192.0'.split('.')))
print(f'{bin(ip[0])[2:].zfill(8)}.{bin(ip[1])[2:].zfill(8)}.{bin(ip[2])[2:].zfill(8)}.{bin(ip[3])[2:].zfill(8)}')

from itertools import *
c = 0
for i in permutations('111000'):
    c += 1
    
print(c)