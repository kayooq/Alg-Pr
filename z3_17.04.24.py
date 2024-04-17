from math import *
x = float(input())
h = float(input())
n = int(input())
s = 0
#PASHALKO SVO 1266
for i in range(0,n+1):
    if abs(cos(x+i*h)) < 0.5:
        s+=1
print(s) 
