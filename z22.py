from math import sin,sqrt,log
k,l,m,x = map(int, input().split())
if m == min(k,l):
    y = sin(abs(x))/sqrt(x**2+1)
    print("y(x) =",y)
elif m == max(k,l):
    y = abs(x)*log(1+x)
    print("y(x) =",y)
elif min(k,l)<m<max(k,l):
    y = x**3+x+10**-2
    print("y(x) =",y)
else:
    y = -1
    print("y(x) =", y)
print("x(y) =", y**4-y**2+5)
