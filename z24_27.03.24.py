from math import sqrt,factorial as fack
e = int(input())
n = 1 
a = [0]
a.append(n/(sqrt((n**2)+1)-sqrt((n**2)-1)))
n+=1
a.append(n/(sqrt((n**2)+1)-sqrt((n**2)-1)))
while abs(a[n]-a[n-1])<e:
    n+=1
    a.append(n/(sqrt((n**2)+1)-sqrt((n**2)-1)))
print('1)',a[n])
a = [0,0.5,0.5*2/3]
n = 2
while abs(a[n]-a[n-1])>e:
    n+=1
    a.append(a[n-1]*(1-(1/n)))
print('2)',a[n])
a = [0,1-1/fack(2),1+1/fack(3)]
n = 2
while abs(a[n]-a[n-1])>e:
    n+=1
    a.append(a[n-1]*(1+(-1**n-1)/(fack(n))))
print('3)',a[n])
