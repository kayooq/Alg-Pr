a = [0]
i = 1
n = int(input('натуральное число '))
while i<=n:
    a.append(i*a[i-1]+1/i)
    i+=1
print(f"значение a с индексом {n}:",a[i-1])
