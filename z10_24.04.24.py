n = int(input('Сколько человек '))
print('1 - английский\n2 - немецкий\n3 - французский\n0 - не изучал')
a = 0
b = 0
c = 0
d = 0
for i in range(1,n+1):
    ch = input(f"Человек номер {i} выбирает:")
    if ch == '1':
        a+=1
    elif ch == '2':
        b+=1
    elif ch == '3':
        c+=1
    elif ch == '0':
        d+=1
print(f'английский: {a}\nнемецкий: {b}\nфранцузский: {c}\nне изучал: {d}')
