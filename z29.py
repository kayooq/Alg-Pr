N = input()
if (int(N) % 100 > 0 and int(N[-2] + N[-1]) % 4 == 0) or (int(N) % 100 == 0 and int(N)%400 ==0):
    print('високосный')
else:
    print('не')
