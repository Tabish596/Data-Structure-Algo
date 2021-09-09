r = {}
def fibo(n):
    
    if n in r:
        return(r[n])
    if n == 1 or n == 2:
        return 1
    r[n] = fibo(n-1)+fibo(n-2)
    return(r[n])


x = fibo(52)
print(x)
