e = 10**-6
a = int(input())
n = 1
x = []
if a <= 1:
    x.append(min(2*a,0.95))
elif 1<a<25:
    x.append(a/5)
else:
    x.append(a/25)
x.append(4/5*x[n-1]+a/(5*x[n-1]**4))
while 5/4*a*(abs(x[n]-x[n-1]))<e:
    n+=1
    x.append(4/5*x[n-1]+a/(5*x[n-1]**4))
print(x[n])
