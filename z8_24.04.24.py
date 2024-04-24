a = int(input())
col = 0
if a > 1:
    for i in range(1,a+1):
        if a%i==0:
            col+=1
if col == 2:
    print(f'число {a} простое')
else:
    print(f"число {a} не простое")
