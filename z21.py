from math import sin,pi,exp,sqrt
x = int(input("x: "))
if x < 0:
    print('1)',4)
if 0<=x<1:
    print("1)",x**2+3*x+4)
if x>1:
    print("1)",x+7)
a = int(input('a: '))
b = int(input("b: "))
if x<0:
    print("2)", sin(x+pi/2)**2)
if a<=x<=b:
    print("2)", exp(x) * sin(x+pi/2))
if x > b: 
    print("2)", sqrt(abs(sin(x+pi/3)))+2.1 * 10**-3)
