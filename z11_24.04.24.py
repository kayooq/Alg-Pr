n = int(input("минимальный номер билета "))
m = int(input("максимальный номер билета "))
lucky = 0
for i in range(n,m+1):
    i = str(i)
    if int(i[0])+int(i[1])+int(i[2]) == int(i[3])+int(i[4])+int(i[5]):
       lucky+=1
print("количество счастливых билетов",lucky)
