def f(n,k):
    if n>k or n==7:
        return 0
    if n==k:
        return 1
    if n<k:
        return f(n+1,k)+f(n+3,k)+f(n*2,k)
print(f(2,15)*f(15,25))
