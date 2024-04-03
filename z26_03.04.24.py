import math
a = int(input())
b = int(input())
e = int(input())
x = [0]
y = [0]
i = 1
x.append(a)
y.append(b)
while abs(x[i]-y[i])<e:
    i+=1
    x.append(1/2*(x[i-1]+y[i-1]))
    y.append(math.sqrt(x[i-1]*y[i-1]))
print(x[i])
