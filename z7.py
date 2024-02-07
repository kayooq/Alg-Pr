from math import sqrt, atan, exp, tan, pi, sin, cos
x = int(input("введите х"))
y = int(input("введите y"))
z = int(input("введите z"))
print("1) a =", (sqrt(abs(x-1)) - abs(y**(1/3))) / (1 + x**2/2 + y**2/4), "b =", x * (atan(z) + exp(-(x+3))))
print("2) a =",(3+exp(y-1))/(1+x**2*abs(y-tan(z))), "b =", 1+abs(y-x)+((y-x)**2/2)+(abs(y-x)**3/3))
print("3) a =", (2*cos(x-pi/6))/(1/2+sin(y)**2), "b =", 1+(z**2)/(3+z**2/5))
