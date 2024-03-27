from math import sqrt
e = int(input())
n = 1 
a = [0]
a.append(n/(sqrt((n**2)+1)-sqrt((n**2)-1)))
n+=1
a.append(n/(sqrt((n**2)+1)-sqrt((n**2)-1)))
while abs(a[n]-a[n-1])<e:
    n+=1
    a.append(n/(sqrt((n**2)+1)-sqrt((n**2)-1)))
print(a[n])
