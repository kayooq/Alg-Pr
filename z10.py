from math import pi, sqrt
R = int(input())
r = int(input())
h = int(input())
l = sqrt(h**2+(R-r)**2)
print("S =", pi*(R+r)*l+pi*R**2+pi*r**2, "V =", 1/3*pi*(R**2+r**2+R*r)*h)
