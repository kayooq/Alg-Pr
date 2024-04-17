from math import sqrt
a = int(input())
b = int(input())
h = int(input())
for x in range(a,b+1,h):
    print('x =',str(x)+':',sqrt(1+2*x+3*x**3) )
