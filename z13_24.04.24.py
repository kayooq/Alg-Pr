q,r,b,c,d = map(float,input("Через пробел ввести действительные числа q,r,b,c,d").split())
n = int(input('натуральное n '))
x=[c,d]
k = 2
while k<=n:
    x.append(q*x[k-1]+r*x[k-2]+b)
    k+=1
print(f"значение x с индексом {n}:",x[k-1])
