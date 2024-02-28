k,l,n,m = map(int, input().split())
if l % k == 0 and n % k == 0 and m % k == 0:
    print(k, "является делителем для этих чисел")
else:
    print("не является")
