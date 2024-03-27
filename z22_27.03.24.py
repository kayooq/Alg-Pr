i=1
e = 0.001
y = [0]
y.append((y[i-1]+1)/(y[i-1]+2))
while abs(y[i]-y[i-1])>e:
    i+=1
    y.append((y[i-1]+1)/(y[i-1]+2))
print(y[i])
