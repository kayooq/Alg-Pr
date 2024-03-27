i=1
e = 0.001
y = [0.001,0]
x = int(input())
y[i]=1/2*(y[i-1]+(x/y[i-1]))
while abs(y[i]-y[i-1])>e:
    i+=1
    y.append(1/2*(y[i-1]+x/y[i-1]))
print(y[i])
