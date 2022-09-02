def Factorial(n):
    f=1
    while(n>1):
        f=f*n
        n=n-1
    return f

def Sum(*a):
    return sum(a)

def SimpleInterest(p,r,t):
    return (p*r*t/100)