n = int(input())
k = []
while n!=0:
    d = 2
    m = n 
    while d * d <= n:
            if n % d == 0:
                k.append(d)
                n//=d
            else:
                d += 1
    k.append(n) 
    print('{} = {}' .format(m, k)) 
    n=int(input())
    k=[]
