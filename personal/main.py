#1
from itertools import permutations
s1 = '457 46 567 12 136 235 13'
s2 = 'FC EGD FGB DA BC EGA FDC'
s2 = {frozenset(x) for x in s2.split()}
print("1 2 3 4 5 6 7")
for p in permutations("ABCDEFG"):
    s3 = s1
    for x, y in zip("1234567", p):
        s3 = s3.replace(x, y)
    s3 = {frozenset(x) for x in s3.split()}
    if s3 == s2:
        print(*p)
#2
print('xyzw')
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((x<=y) and (not(y)==z) and w)==1:
                    print(x,y,z,w)
#5
for n in range(1,400):
    r=bin(n)[2:]
    sm=(r.count('1'))
    if sm%2==0:
        r='10'+r[2:]+'0'
    else:
        r='11'+r[2:]+'1'
    r=int(r,2)
    if r>480:
        print(n)
        break
#6
        from turtle import*
k=10
tracer(0)
for i in range(9):
    fd(22*k)
    right(90)
    fd(6*k)
    rt(90)
penup()
fd(1*k)
rt(90)
fd(5*k)
left(90)
pendown()
for i in range(9):
    fd(53*k)
    rt(90)
    fd(75*k)
    rt(90)
penup()
for x in range(-75,75):
    for y in range(-75,75):
        setpos(x*k,y*k)
        dot(2)
done()


#9
f = open('99.txt').readlines()   
c = 0                           
for i in f:                     
    i = i.split('\t')           
    i = list(map(int, i))       
    pov1=[k for k in i if i.count(k) == 1]
    b=max(i)
    t=min(i)
    v=sum(b,t)
    y=sum(i)-v
    i = sorted(i)              
    if v>y: 
        c += 1                 
print(c)    

#19
def f(a, s, p):
    if a + s >= 65 and p == 3:
        return True
    if a + s >= 65 and p == 2:
        return False
    if a + s < 65 and p == 3:
        return False
    if p % 2 == 0:
        return f(a+1, s, p+1) or f(a*3, s, p+1) or f(a, s+1, p+1) or f(a, s*3, p+1)
    if p % 2 == 1:
        return f(a+1, s, p+1) or f(a*3, s, p+1) or f(a, s+1, p+1) or f(a, s*3, p+1)
for s in range(1,58):
    if f(6, s, 1) == True:
        print(s)
        #20
        def f(a, s, p):
    if a + s >= 65 and p == 4:
        return True
    if a + s >= 65 and p == 3:
        return False
    if a + s < 65 and p == 4:
        return False
    if p % 2 == 1:
        return f(a+1, s, p+1) or f(a*3, s, p+1) or f(a, s+1, p+1) or f(a, s*3, p+1)
    if p % 2 == 0:
        return f(a+1, s, p+1) and f(a*3, s, p+1) and f(a, s+1, p+1) and f(a, s*3, p+1)
for s in range(1,58):
    if f(6, s, 1) == True:
        print(s)
        

        #21
        def f(a, s, p):
    if a + s >= 65 and (p == 3 or p == 5):
        return True
    if a + s >= 65 and (p == 2 or p == 4):
        return False
    if a + s < 65 and p == 5:
        return False
    if p % 2 == 0:
        return f(a+1, s, p+1) or f(a*3, s, p+1) or f(a, s+1, p+1) or f(a, s*3, p+1)
    if p % 2 == 1:
        return f(a+1, s, p+1) and f(a*3, s, p+1) and f(a, s+1, p+1) and f(a, s*3, p+1)
for s in range(1,58):
    if f(6, s, 1) == True:
        print(s)
