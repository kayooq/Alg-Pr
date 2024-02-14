from math import sqrt
a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
print("r =", sqrt(((p-a)*(p-b)*(p-c))/p), "R =", (a*b*c)/(4*sqrt(p*(p-a)*(p-b)*(p-c))))
