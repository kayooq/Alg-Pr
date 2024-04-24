n = int(input("всего товарааааааааааааааа "))
z = int(input("цена одного товара "))
s = int(input("денег у одного "))
k = int(input('покупателей '))
while n>0 and k>0:

    for i in range(1,k+1):
        if n == 0:
            print('Товар кончился')
            break
        buy = int(input(f"Покупатель {i} купил столько товара "))
        if buy*z<=s:
            n-=buy
            print(f'Осталось {n} единиц товара')
            k-=1
        if k == 0:
            print('Покупателей больше нет')
            break
