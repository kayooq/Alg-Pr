i=1
e = 0.001
x = [1]
x.append((2-x[i-1]**3)/5)
while abs(x[i]-x[i-1])>e:
    i+=1
    x.append((2-x[i-1]**3)/5)
print(x[i])
