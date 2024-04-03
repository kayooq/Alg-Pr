x = int(input())
b = []
max = x
min = x
while x!=0:
    b.append(x)
    if x > max:
        max=x
    if x < min:
        min=x
    x = int(input())
print('диапозон:',str(max)+'-'+str(min))
print('наименьшее число',min,'по счету',b.index(min)+1)
